import streamlit as st
from PIL import Image

def main():
    st.title("병원소개 페이지")
    st.subheader("서울 탈모병원의 시설과 의료진을 소개합니다.")
    
    st.image("images/병원외관.jpg", caption="병원 외관", width=450)
    st.image("images/의료진.jpg", caption="의료진", width=450)
    st.image("images/병원시설.jpg", caption="병원 시설", width=450)

if __name__ == "__main__":
    main()
