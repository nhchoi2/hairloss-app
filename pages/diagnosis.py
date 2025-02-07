import streamlit as st
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

def main():
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
        
    # 가장 높은 확률을 가진 라벨 찾기
    labels = ["M자 탈모", "탈모", "정상"]
    max_index = np.argmax(prediction)  # 가장 높은 확률을 가진 인덱스 찾기
    max_label = labels[max_index]  # 해당 인덱스에 해당하는 라벨
    max_confidence = prediction_percent[max_index]  # 해당 라벨의 확률

    # 결과 표시
    st.write(f"진단 결과: {max_label} ({max_confidence}%)")
        
if __name__ == "__main__":
    main()
