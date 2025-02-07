import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import load_model
from PIL import Image, ImageOps
from datetime import datetime
import os

# 데이터 폴더가 없으면 생성
if not os.path.exists("data"):
    os.makedirs("data")

def save_to_history(user_id, gender, age, test_date, diagnosis, user_notes):
    """입력된 데이터를 CSV 파일에 저장 (pd.concat() 방식 적용)"""
    file_path = "data/hair_loss_records.csv"

    # 새로운 데이터 생성
    new_data = pd.DataFrame([{
        "user_id": user_id,
        "gender": gender,
        "age": age,
        "test_date": test_date,
        "max_label": diagnosis,
        "user_notes": user_notes
    }])

    # 기존 파일이 있으면 로드 후 데이터 추가, 없으면 새로 생성
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, new_data], ignore_index=True)  # 데이터 추가
    else:
        df = new_data  # 첫 데이터 저장

    # CSV 파일로 저장
    df.to_csv(file_path, index=False)
    st.success("✅ 검사 결과가 CSV 파일에 저장되었습니다!")

def main():
    st.title("AI 탈모 진단")
    model = load_model("model/keras_model.h5")  # AI 모델 로드

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

        # 검사 결과 저장 폼을 항상 표시
        with st.form("user_input_form"):
            user_id = st.text_input("User ID", "")
            gender = st.radio("성별", ["남", "여"])
            age = st.number_input("나이", min_value=1, max_value=100, step=1)
            test_date = st.text_input("검사일자", datetime.today().strftime('%Y-%m-%d'), disabled=True)
            user_notes = st.text_area("사용자 입력 추가 정보 (선택)")
            
            # 폼 제출 버튼
            submit_button = st.form_submit_button("저장")

            if submit_button:
                st.write("✅ 저장 버튼이 클릭되었습니다!")  # 버튼 클릭 확인
                save_to_history(user_id, gender, age, test_date, max_label, user_notes)
                st.success("✅ 검사 결과가 저장되었습니다!")
                st.rerun()  # 최신 Streamlit에서는 st.experimental_rerun() 대신 st.rerun() 사용

if __name__ == "__main__":
    main()
