# streamlit_layout.py

import streamlit as st

st.title("등록 양식")

first, last = st.columns(2)
first.text_input("성")
last.text_input("이름")

email, social_number = st.columns([2, 7])
email.text_input("email 주소")
social_number.text_input("주민등록번호")

user, pw, pw2 = st.columns(3)
user.text_input("사용자 이름")
pw.text_input("패스워드", type = "password")
pw2.text_input("패스워드 확인", type = "password")

ch, bl, sub = st.columns(3)
ch.checkbox("동의")
sub.button("제출")