import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_history():
    """진단 기록을 CSV에서 불러오기"""
    try:
        df = pd.read_csv("data/hair_loss_records.csv")
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["User ID", "성별", "나이", "검사일자", "검사결과", "사용자 입력 추가 정보"])

def display_history():
    """진단 기록을 테이블로 표시"""
    df = load_history()
    if df.empty:
        st.warning("아직 저장된 기록이 없습니다.")
    else:
        st.subheader("📜 지난 검사 기록")
        st.dataframe(df)

def plot_progress():
    """탈모 진행률 변화를 그래프로 표시"""
    df = load_history()
    if df.empty:
        return
    
    df["검사일자"] = pd.to_datetime(df["검사일자"])
    df = df.sort_values("검사일자")
    
    type_mapping = {"M자 탈모": 2, "탈모": 1, "정상": 0}
    df["진단결과수치"] = df["검사결과"].map(type_mapping)
    
    fig, ax = plt.subplots()
    ax.plot(df["검사일자"], df["진단결과수치"], marker='o', linestyle='-', color='red')
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(["정상", "탈모", "M자 탈모"])
    ax.set_xlabel("검사일자")
    ax.set_ylabel("진단 결과")
    ax.set_title("탈모 진행률 변화")
    st.pyplot(fig)

def main():
    st.title("📊 탈모 검사 기록")
    display_history()
    
    if not load_history().empty:
        st.subheader("📈 탈모 진행률 변화")
        plot_progress()

if __name__ == "__main__":
    main()