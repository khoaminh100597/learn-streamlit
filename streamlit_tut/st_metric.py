import streamlit as st

col1, col2, col3 = st.columns(3)

col1.metric('Temperature', "70 °F", delta="1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.metric(
    label='Gas Price',
    value=4,
    delta=-0.5,
    delta_color='inverse'
)

st.metric(
    label='Active developers',
    value=123,
    delta=123,
    delta_color='off'
)