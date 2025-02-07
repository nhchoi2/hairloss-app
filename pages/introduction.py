import streamlit as st
from PIL import Image

def main():
    st.title("🏥 병원 소개")
    st.subheader("서울 탈모병원의 시설과 의료진을 소개합니다.")

    # 병원 외관 + 소개
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("images/병원외관.jpg", caption="병원 외관", width=400)
    with col2:
        st.markdown("""
        ### 서울 탈모병원 소개
        서울 탈모병원은 최신 탈모 치료 기술을 도입하여 환자 맞춤형 치료를 제공합니다.  
        과학적으로 검증된 치료법과 숙련된 의료진이 환자 한 분 한 분의 상태에 맞춰  
        최적의 솔루션을 제공합니다.  
        """)

    # 의료진 + 소개
    st.markdown("---")
    col3, col4 = st.columns([1, 2])
    with col3:
        st.image("images/의료진.jpg", caption="의료진", width=400)
    with col4:
        st.markdown("""
        ### 의료진 소개
        본원에는 탈모 치료 경험이 풍부한 전문 의료진이 상주하고 있으며,  
        최신 연구와 임상 결과를 바탕으로 환자 개개인에게 최적의 치료 방법을 제공합니다.  
        꾸준한 연구와 환자 중심의 치료를 통해 신뢰받는 병원이 되도록 노력하고 있습니다.
        """)

    # 병원 시설 + 소개
    st.markdown("---")
    col5, col6 = st.columns([1, 2])
    with col5:
        st.image("images/병원시설.jpg", caption="병원 시설", width=400)
    with col6:
        st.markdown("""
        ### 최신 시설 및 편의 제공
        서울 탈모병원은 최첨단 의료 장비를 보유하고 있으며,  
        쾌적한 환경에서 환자가 편안하게 치료를 받을 수 있도록 다양한 편의시설을 갖추고 있습니다.  
        개인 맞춤형 상담실, 최신형 시술 장비, 청결한 진료 공간을 통해  
        최상의 치료 환경을 제공합니다.
        """)

if __name__ == "__main__":
    main()
