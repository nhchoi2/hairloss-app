import streamlit as st
import time  # ⬅ 새로 추가
import pandas as pd
from datetime import datetime

def save_to_history(user_id, gender, age, test_date, diagnosis, user_notes):
    """입력된 데이터를 CSV 파일에 저장"""
    file_path = "data/hair_loss_records.csv"
    if not os.path.exists("data"):
        os.makedirs("data")
    
    try:
        df = pd.read_csv(file_path)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.DataFrame(columns=["User ID", "성별", "나이", "검사일자", "검사결과", "사용자 입력 추가 정보"])
    
    new_data = pd.DataFrame([[user_id, gender, age, test_date, diagnosis, user_notes]],
                            columns=["User ID", "성별", "나이", "검사일자", "검사결과", "사용자 입력 추가 정보"])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(file_path, index=False)

def main():
    st.title("AI 탈모 진단")

    with st.form("user_input_form"):
        user_id = st.text_input("User ID", "")
        gender = st.radio("성별", ["남", "여"])
        age = st.number_input("나이", min_value=1, max_value=100, step=1)
        test_date = st.text_input("검사일자", datetime.today().strftime('%Y-%m-%d'), disabled=True)
        user_notes = st.text_area("사용자 입력 추가 정보 (선택)")
        submit_button = st.form_submit_button("저장")

        if submit_button:
            st.write("✅ 저장 버튼이 클릭되었습니다!")
            save_to_history(user_id, gender, age, test_date, "AI 진단 결과", user_notes)
            st.success("✅ 검사 결과가 저장되었습니다!")
            
            # 🔹 테이블 표시 (잠시 보여주고 히스토리 페이지로 이동)
            st.write("📂 저장된 데이터 확인:")
            df = pd.read_csv("data/hair_loss_records.csv")
            st.dataframe(df)
            
            time.sleep(2)  # ⬅ 2초 동안 테이블을 표시한 후 히스토리 페이지로 이동
            st.switch_page("history.py")  # ✅ 히스토리 페이지로 이동

if __name__ == "__main__":
    main()
