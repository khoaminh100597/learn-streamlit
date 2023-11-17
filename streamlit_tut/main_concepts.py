import streamlit as st
import pandas as pd
import numpy as np
import time

# create data
dataframe = pd.DataFrame(
    np.random.rand(10, 20),
    columns=('col %d' % i for i in range(20))
)

chart_data = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

map_data = pd.DataFrame(
    np.random.rand(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

# st.dataframe()
st.dataframe(dataframe.style.highlight_max(axis=0))

# st.table()
st.table(dataframe)

# st.line_chart()
st.line_chart(chart_data)

# st.map()
st.map(map_data)

# widgets
x = st.slider('x')
st.write(x, 'squared is', x*x)

st.text_input('Your name', key='name')
st.write(st.session_state.name)

# st.checkbox()
if st.checkbox('Show dataframe'):
    st.line_chart(chart_data)

# st.selectbox()
option = st.selectbox('Which column do you want to display',
                      chart_data.columns)
st.write(option)

# add a selectbox to the sidebar
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted',
    ('Email', 'Home phone', 'Mobile phone')
)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# use st.columns()
left_column, right_column = st.columns(2)

left_column.button('Press me!')

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
    )
    st.write(f'You are in {chosen} hat')

with st.expander('See explaination'):
    st.write('Hello World')

'Starting a long computation...'

# add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i+1)
    time.sleep(0.1)

'... and now we\'re done!'