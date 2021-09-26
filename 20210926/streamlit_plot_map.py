# streamlit_plot.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

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

chart = alt.Chart(data).mark_circle().encode(
    x = "a", y = "b", tooltip = ["a", "b"]
)
st.altair_chart(chart, use_container_width = True)

city = pd.DataFrame({
    "멋진 도시": ["시카고", "미네아폴리스", "루이스빌", "토페가"],
    "lat" : [41.868171, 44.979840, 38.257972, 39.030575],
    "lon" : [-87.667458, -93.272474, -85.765187, -95.702548]
})
st.table(city)
st.map(city)

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