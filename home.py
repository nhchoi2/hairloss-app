import streamlit as st
from PIL import Image

def main():
    # App 설정
    st.set_page_config(page_title="슬기로운 탈모병원", layout="wide")
    # 사이드바
    with st.sidebar:
        st.image("images/sidebar_bg.png", caption="슬기로운 탈모병원", width=300)
        st.markdown("**병원 연락처:**")
        st.markdown("전화: 02-123-4567")
        st.markdown("[병원 블로그 바로가기](https://boohoday.com/)")

    # 로고와 병원명을 한 줄로 정렬
    col_logo, col_title = st.columns([1, 5])  # 로고 1, 타이틀 5 비율

    with col_logo:
        st.image("images/hospital_logo.png", width=50)  # 병원 로고 (크기 조정 가능)

    with col_title:
        st.markdown("<h1 style='display: flex; align-items: center;'>슬기로운 탈모병원</h1>", unsafe_allow_html=True)

    st.subheader("AI 기반 탈모 진단 & 맞춤 관리 가이드")
    st.image("images/병원외관.jpg", caption="슬기로운 탈모병원", width=300)

    # 메인화면 구성
    st.markdown("---")
    col = st.columns(3)  # 3개의 컬럼 생성

    with col[0]:  # 첫 번째 컬럼
        st.image("images/diagnosis_example.png", caption="M자 탈모", use_container_width=True)

    with col[1]:  # 두 번째 컬럼
        st.image("images/원형탈모.jpeg", caption="원형탈모", use_container_width=True)

    with col[2]:  # 세 번째 컬럼
        st.image("images/반흔.jpeg", caption="반흔성 탈모", use_container_width=True)



if __name__ == "__main__":
    main()
