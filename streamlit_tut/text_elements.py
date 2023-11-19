import streamlit as st
import numpy as np
import pandas as pd
from annotated_text import annotated_text

st.title('This is a title')
st.divider()
st.header('This is a header')
st.divider()
st.subheader('This is a subheader')
st.divider()
st.caption('This is a caption')
st.divider()
st.code("""
    a = 123
    def printa():
        print(a)
""", language='python')
st.divider()
st.text('This is from st.text()')
st.divider()
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
st.divider()
annotated_text('This is some ', ('annotated words', 'in the websited'))