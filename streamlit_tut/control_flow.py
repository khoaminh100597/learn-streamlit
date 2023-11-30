import streamlit as st
import numpy as np
import pandas as pd

name = st.text_input('Please input name')
if not name:
    st.warning('Please input a name')
    st.stop()
st.success('Thank you for inputting a name.')

with st.form('My form'):
    st.write('Inside the form')
    slider_val = st.slider('Form slider')
    checkbox_val = st.checkbox('Form checkbox')

    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.write('Slider', slider_val, 'checkbox', checkbox_val)

if "value" not in st.session_state:
    st.session_state.value = "Title"

##### Option using st.rerun #####
st.header(st.session_state.value)

if st.button("Foo"):
    st.session_state.value = "Foo"
    st.rerun()

st.write('Outside the form')