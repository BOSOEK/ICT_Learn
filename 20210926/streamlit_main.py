# streamlit_main.py
import streamlit as st

st.title("안녕하세요!")
st.header("header")
st.subheader("subheader")
st.text("이것은 일반 텍스트")

st.markdown("""
# h1 tag
## h2 tag
### h3 tag
:moon:<br>
<h1>fefef</h1>
:sunglasses:
** bold **
_ italics _
""", True)

st.latex(r""" a + ar + a r^2 + a r^3 + \cdots + a r^{n - 1} = 
\sum_{k=0}^{n-1} ar^k =
a \left(\frac{1-r^{n}}{1-r}\right) 
""")

d = {
    "name": "Harsh",
    "language": "Python",
    "topic": "Streamlit"
}
st.write(d)