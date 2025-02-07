import streamlit as st
import pandas as pd
import os

def load_history():
    """진단 기록을 CSV에서 불러오기"""
    file_path = "data/hair_loss_records.csv"

    # 파일이 없으면 빈 데이터프레임 생성
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        st.warning("⚠ CSV 파일이 없거나 비어 있습니다.")
        df = pd.DataFrame(columns=["User ID", "성별", "나이", "검사일자", "검사결과", "사용자 입력 추가 정보"])
        df.to_csv(file_path, index=False)
        return df
    
    return pd.read_csv(file_path)

def main():
    st.title("📊 탈모 검사 내역 확인")
    st.subheader("👤 이름과 성별, 나이를 입력해 주세요")

    df = load_history()
    
    # 유저 정보 입력 필터
    user_id = st.text_input("이름을 입력하세요")
    gender = st.radio("성별 선택", ["남", "여"])
    age = st.number_input("나이 입력", min_value=1, max_value=100, step=1)
    
    # 조회 버튼 추가
    if st.button("조회"):
        # 조건에 맞는 데이터 불러오기 (최대 10개)
        filtered_df = df[(df["User ID"] == user_id) & (df["성별"] == gender) & (df["나이"] == age)]
        filtered_df = filtered_df.tail(10)  # 최신 10개 데이터만 표시

        if filtered_df.empty:
            st.warning("해당 조건에 맞는 데이터가 없습니다.")
            return
        
        # 데이터프레임 표시
        st.subheader("📋 조회된 검사 기록")
        st.dataframe(filtered_df[["검사일자", "검사결과", "사용자 입력 추가 정보"]])

        # 최근 데이터 표로 표시
        latest_data = filtered_df.iloc[-1]  # 최신 데이터 선택
        st.subheader("🔍 최근 검사 기록")
        st.table(latest_data[["검사일자", "검사결과", "사용자 입력 추가 정보"]])

if __name__ == "__main__":
    main()
