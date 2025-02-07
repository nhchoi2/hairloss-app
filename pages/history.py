import streamlit as st
import pandas as pd
import os

def load_history():
    """진단 기록을 CSV에서 불러오기"""
    file_path = "data/hair_loss_records.csv"

    # 파일이 없거나 비어 있으면 새로 생성
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        st.warning("⚠ CSV 파일이 없거나 비어 있습니다. 새로 생성합니다.")
        df = pd.DataFrame(columns=["User ID", "성별", "나이", "검사일자", "검사결과", "사용자 입력 추가 정보"])
        df.to_csv(file_path, index=False)
        return df

    try:
        df = pd.read_csv(file_path)
        return df
    except pd.errors.EmptyDataError:
        st.error("⚠ CSV 파일이 비어 있습니다. 새로 생성합니다.")
        df = pd.DataFrame(columns=["User ID", "성별", "나이", "검사일자", "검사결과", "사용자 입력 추가 정보"])
        df.to_csv(file_path, index=False)
        return df

def save_user_info(user_id, gender, age):
    """새로운 유저 정보를 기록"""
    file_path = "data/hair_loss_records.csv"
    df = load_history()

    # 기존 데이터에서 유저 ID가 존재하는지 확인
    if user_id in df["User ID"].values:
        st.warning("⚠ 이미 존재하는 User ID입니다. 다른 ID를 입력하세요.")
        return
    
    new_data = pd.DataFrame([[user_id, gender, age, "-", "-", "-"]],
                            columns=["User ID", "성별", "나이", "검사일자", "검사결과", "사용자 입력 추가 정보"])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(file_path, index=False)
    st.success("✅ 유저 정보가 저장되었습니다!")

def display_history():
    """진단 기록을 테이블로 표시"""
    df = load_history()
    if df.empty:
        st.warning("아직 저장된 기록이 없습니다.")
    else:
        st.subheader("📜 지난 검사 기록")
        st.dataframe(df)

def main():
    st.title("📊 탈모 검사 기록")
    
    # 유저 정보 입력 폼
    with st.form("user_info_form"):
        user_id = st.text_input("User ID", "")
        gender = st.radio("성별", ["남", "여"])
        age = st.number_input("나이", min_value=1, max_value=100, step=1)
        submit_button = st.form_submit_button("유저 정보 저장")
        
        if submit_button:
            save_user_info(user_id, gender, age)
            st.experimental_rerun()

    display_history()

if __name__ == "__main__":
    main()
