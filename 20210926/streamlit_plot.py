# streamlit_plot.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.graphviz_chart("""
    digraph {
        run -> intr
        intr -> runbl
    }
""")

data = pd.DataFrame(
    np.random.randn(100, 3),
    columns = ["a", "b", "c"]
)

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.scatter(data["a"], data["b"])
plt.title("scatter")
st.pyplot()

st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)

st.image("office_view.jpg")
st.audio("demo.wav")
st.video("office_view.mp4")
st.video("https://www.youtube.com/watch?v=e9VmlEqU7ZU")