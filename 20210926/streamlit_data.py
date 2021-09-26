# streamlit_data.py
import streamlit as st
import pandas as pd
import numpy as np
import time

a = [1, 2, 3, 4, 5, 6, 7, 8]
n = np.array(a)
nd = n.reshape((2, 4))
dic = {
    "name": ["영희", "철수"],
    "age": [21, 32],
    "city": ["서울", "수원"]
}

data = pd.read_csv("Salary_Data.csv")
print(data)

st.dataframe(a)
st.dataframe(n)
st.dataframe(nd)
st.dataframe(dic)
st.dataframe(data, width = 500, height = 500)
st.table(data)
st.json(dic)
st.write(data)


