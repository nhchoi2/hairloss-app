import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import load_model
from PIL import Image, ImageOps
from datetime import datetime

def save_to_history(user_id, gender, age, test_date, diagnosis, user_notes):
    """입력된 데이터를 CSV 파일에 저장"""
    file_path = "data/hair_loss_records.csv"
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["User ID", "성별", "나이", "검사일자", "검사결과", "사용자 입력 추가 정보"])
    
    new_data = pd.DataFrame([[user_id, gender, age, test_date, diagnosis, user_notes]],
                            columns=["User ID", "성별", "나이", "검사일자", "검사결과", "사용자 입력 추가 정보"])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(file_path, index=False)

def main():
    st.title("AI 탈모 진단")
    model = load_model("model/keras_model.h5")

    file = st.file_uploader("사진을 업로드해주세요", type=["jpg", "png", "jpeg"])
    
    if file is not None:
        image = Image.open(file)
        st.image(image, caption="업로드된 이미지", width=450)

        # 이미지 전처리 및 모델 예측
        image = ImageOps.fit(image, (224, 224))
        img_array = np.asarray(image) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)[0]  # 예측 결과 가져오기
        prediction_percent = (prediction * 100).astype(int)  # 확률 값을 정수(%)로 변환

        labels = ["M자 탈모", "탈모", "정상"]
        max_index = np.argmax(prediction)  # 가장 높은 확률을 가진 인덱스 찾기
        max_label = labels[max_index]  # 해당 인덱스에 해당하는 라벨
        max_confidence = prediction_percent[max_index]  # 해당 라벨의 확률

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
