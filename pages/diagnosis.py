import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 데이터 폴더가 없으면 생성
if not os.path.exists("data"):
    os.makedirs("data")

def save_to_history(user_id, gender, age, test_date, diagnosis, user_notes):
    """입력된 데이터를 CSV 파일에 저장 (pd.append() 방식 적용)"""
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

    # 사용자 입력 폼
    with st.form("user_input_form"):
        user_id = st.text_input("User ID", "")
        gender = st.radio("성별", ["남", "여"])
        age = st.number_input("나이", min_value=1, max_value=100, step=1)
        test_date = st.text_input("검사일자", datetime.today().strftime('%Y-%m-%d'), disabled=True)
        user_notes = st.text_area("사용자 입력 추가 정보 (선택)")
        
        submit_button = st.form_submit_button("저장")

        if submit_button:
            st.write("✅ 저장 버튼이 클릭되었습니다!")  # 디버깅용 로그 출력
            save_to_history(user_id, gender, age, test_date, "AI 진단 결과", user_notes)
            st.success("✅ 검사 결과가 저장되었습니다!")
            st.rerun()  # 최신 Streamlit에서는 st.experimental_rerun() 대신 st.rerun() 사용

if __name__ == "__main__":
    main()
