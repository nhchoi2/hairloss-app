import streamlit as st
from PIL import Image

def main():
    # App 설정
    st.set_page_config(page_title="서울 탈모병원", layout="wide")

    # 사이드바
    with st.sidebar:
        st.image("images/sidebar_bg.png", caption="병원 데스크", width=300)
        st.markdown("**병원 연락처:**")
        st.markdown("전화: 02-123-4567")
        st.markdown("[병원 블로그 바로가기](https://example.com)")

    # 메인화면 상단
    st.title("서울 탈모병원")
    st.subheader("AI 기반 탈모 진단 & 맞춤 관리 가이드")

    # 상단 링크 메뉴
    st.markdown("---")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("[병원소개 페이지](pages/introduction.py)")
    with col2:
        st.markdown("[오시는길](https://maps.google.com)")
    with col3:
        st.markdown("[탈모설명](pages/hair_loss_intro.py)")
    with col4:
        st.markdown("[탈모관리법](pages/info.py)")
    with col5:
        st.markdown("[탈모진단테스트](pages/diagnosis.py)")

    # 메인화면 구성
    st.markdown("---")
    col1, col2 = st.columns([1, 1])

    with col1:
        st.button("AI 탈모 진단 시작하기", on_click=lambda: st.experimental_rerun())
        st.button("지난 검사 결과 보기", on_click=lambda: st.experimental_rerun())
    
    with col2:
        st.image("images/diagnosis_example.png", caption="탈모 진단 예시", width=450)

if __name__ == "__main__":
    main()
