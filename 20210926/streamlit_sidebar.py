# streamlit_sidebar.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

data = {
    "num": [x for x in range(1, 11)],
    "square": [x**2 for x in range(1, 11)],
    "twice": [x*2 for x in range(1, 11)],
    "thrice": [x*3 for x in range(1, 11)]
}

df = pd.DataFrame(data)

rad = st.sidebar.radio("네비게이션", ["Home", "About Us"])

if rad == "Home":
    col1 = st.sidebar.selectbox("컬럼을 선택해주세요", df.columns)
    plt.plot(df["num"], df[col1])
    st.pyplot()

    col2 = st.sidebar.multiselect("컬럼을 선택해주세요", df.columns)
    plt.plot(df["num"], df[col2])
    st.pyplot()
elif rad == "About Us":
    st.sidebar.selectbox("숫자를 선택해 주세요", [1, 2, 3, 4, 5]) 