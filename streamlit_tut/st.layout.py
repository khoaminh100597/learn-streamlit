import streamlit as st
import numpy as np 
import time

with st.sidebar:
    add_radio = st.radio(
        'Choose a shipping method',
        ('Standard (5-15 days)', 'Express (2-5 days)')
    )

    with st.echo():
        st.write('This code will be printed to the sidebar')

    with st.spinner('Loading...'):
        time.sleep(5)
    st.success('Done')

col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader('A wide column with a chart')
col1.line_chart(data)

col2.subheader('A narrow column with the data')
col2.write(data)

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

with tab1:
    st.subheader('A tab with a chart')
    st.line_chart(data)
with tab2:
    st.subheader('A tab with the data')
    st.write(data)

st.divider()

# st.expander()
with st.expander('See explaination'):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)

st.divider()

# st.container()
with st.container():
    st.write('This is inside the container')

    # You can call any Streamlit command, including custom components
    st.bar_chart(np.random.randn(50, 3))

st.divider()

# st.empty()
placeholder = st.empty()

placeholder.text('Hello')

placeholder.line_chart(np.random.randn(20, 3))

# with placeholder.container():
#     st.write('This is one element')
#     st.write('This is another')

