import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
from PIL import Image, ImageOps

# 글꼴 설치 os 시작 ---------------
import os
import matplotlib.font_manager as fm

@st.cache_data
def fontRegistered():
    font_dirs = [os.getcwd() + '/custom_fonts']
    font_files = fm.findSystemFonts(fontpaths=font_dirs)
    for font_file in font_files:
        fm.fontManager.addfont(font_file)
    fm._load_fontmanager(try_read_cache=False)
# 글꼴 설치 os 끝 ---------------

def main():
    # 글꼴 추가 시작 ---------------
    fontRegistered()
    plt.rc('font', family='NanumBarunGothic')
    # 글꼴 추가 끝 ---------------

    st.title("AI 탈모 진단")
    st.subheader(" 탈모사진 업로드 예시 ")
    col = st.columns(3)  # 3개의 컬럼 생성
    
    with col[0]:  # 첫 번째 컬럼
        st.image("images/diagnosis_example.png", caption="M자 탈모", width=150)

    with col[1]:  # 두 번째 컬럼
        st.image("images/원형탈모.jpeg", caption="원형탈모", width=150)

    with col[2]:  # 세 번째 컬럼
        st.image("images/반흔.jpeg", caption="반흔성 탈모", width=150)
    st.markdown("---")

    model = load_model("model/keras_model.h5")
    
    file = st.file_uploader("사진을 업로드해주세요", type=["jpg", "png", "jpeg"])
    if file is not None:
        image = Image.open(file)
        st.image(image, caption="업로드된 이미지", width=450)
        
        # 이미지 전처리 및 모델 예측
        image = ImageOps.fit(image, (224, 224))
        img_array = np.asarray(image) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        prediction = model.predict(img_array)[0]  # 예측 결과 배열 가져오기
        prediction_percent = (prediction * 100).astype(int)  # 확률 값을 정수(%)로 변환
        
        # 결과 표시
        # 가장 높은 확률을 가진 라벨 찾기
        labels = ["M자 탈모", "탈모", "정상"]
        max_index = np.argmax(prediction)  # 가장 높은 확률을 가진 인덱스 찾기
        max_label = labels[max_index]  # 해당 인덱스에 해당하는 라벨
        max_confidence = prediction_percent[max_index]  # 해당 라벨의 확률

        # 결과 표시
        st.write(f"### 🩺 진단 결과: {max_label} ({max_confidence}%)")

          # 검사 결과 저장 버튼 생성
        if st.button("검사 결과를 저장하시겠습니까?"):
            with st.form("user_input_form"):
                user_id = st.text_input("User ID", "")
                gender = st.radio("성별", ["남", "여"])
                age = st.number_input("나이", min_value=1, max_value=100, step=1)
                test_date = st.text_input("검사일자", datetime.today().strftime('%Y-%m-%d'), disabled=True)
                user_notes = st.text_area("사용자 입력 추가 정보 (선택)")
                submit_button = st.form_submit_button("저장")
                
                if submit_button:
                    save_to_history(user_id, gender, age, test_date, max_label, user_notes)
                    st.success("검사 결과가 저장되었습니다!")
                    st.experimental_rerun()

if __name__ == "__main__":
    main()
