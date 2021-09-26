# streamlit_widget.py
import streamlit as st

st.title("위젯들 알아보기")

if st.button("눌러보세요"):
    st.write("눌려졌군요")

name = st.text_input("이름 입력")
st.write(name)

address = st.text_area("주소 입력")
st.write(address)

st.date_input("날짜 입력")

st.time_input("시간 입력")

if st.checkbox("체크하면 어떻게 될까?", value = True):
    st.write("감사합니다")

v1 = st.radio("색", ["r", "g", "b"], index = 1)
v2 = st.selectbox("색", ["r", "g", "b"], index = 2)

st.write(v1, v2)

v3 = st.multiselect("색", ["r", "g", "b"])
st.write(v3)

st.slider("나이", min_value = 18, max_value=60, value =30, step = 2)

st.number_input("숫자", min_value=18.0, max_value=60.0, value=30.0, step=2.0)

img = st.file_uploader("파일 업로드")
st.image(img)