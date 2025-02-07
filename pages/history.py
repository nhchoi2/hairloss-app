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
    
    # 조건에 맞는 데이터 10개만 불러오기
    filtered_df = df[(df["User ID"] == user_id) & (df["성별"] == gender) & (df["나이"] == age)]
    filtered_df = filtered_df.tail(10)  # 최대 10개만 가져오기
    
    if filtered_df.empty:
        st.warning("해당 조건에 맞는 데이터가 없습니다.")
        return
    
    # 인덱스 클릭을 위한 컬럼 추가
    filtered_df = filtered_df.reset_index()
    filtered_df["보기"] = [f"표로 보기" for _ in range(len(filtered_df))]
    
    # 데이터프레임 표시
    selected_index = st.data_editor(
        filtered_df[["검사일자", "검사결과", "사용자 입력 추가 정보", "보기"]],
        column_config={"보기": st.column_config.ButtonColumn("보기")},
        hide_index=True
    )
    
    # 선택된 인덱스의 데이터 표시
    if selected_index is not None:
        st.subheader("🔍 선택한 검사 기록")
        selected_data = filtered_df.iloc[selected_index]
        st.table(selected_data[["검사일자", "검사결과", "사용자 입력 추가 정보"]])

if __name__ == "__main__":
    main()
