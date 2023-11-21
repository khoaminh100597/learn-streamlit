import streamlit as st
import pandas as pd
import numpy as np
from datetime import time, datetime

# st.button()
st.button('Reset', type='primary')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye!')

st.divider()

# st.download_button()
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
@st.cache_data
def convert_df(df):
    return df.to_csv().encode('utf-8')
st.download_button(
    label='Download data as CSV',
    data=convert_df(df),
    file_name='large_df.csv',
    mime='text/csv'
)

text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

binary_contents = b'example content'
st.download_button('Download binary file', binary_contents)

st.divider()

# st.link_button()
st.link_button('Go to gallery', 'https://streamlit.io/gallery')

st.divider()

# st.checkbox()
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

st.divider()

# st.toggle()
on = st.toggle('Activate feature')
if on:
    st.write('Feature activated!')

st.divider()

# st.radio()
genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."]
)

if genre == ':rainbow[Comedy]':
    st.write('You selected comedy.')
else:
    st.write('You didn\'t select comedy')

if 'visibility' not in st.session_state:
    st.session_state.visibility = 'visible'
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2, = st.columns(2)

with col1:
    st.checkbox('Disable radio widget', key='disabled')
    st.checkbox('Orient radion options horizontally', key='horizontal')
with col2:
    st.radio(
        'Set label visibility',
        ['visible', 'hidden', 'collapsed'],
        key='visibility',
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal
    )

st.divider()

# st.selectbox()
option = st.selectbox(
    'How would you like to be contacted',
    ('Email', 'Home phone', 'Mobile phone'),
    index=None,
    placeholder='Select contact method...'
)
st.write('You selected: ', option)

st.divider()

# st.multiselect()
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)
st.write('You selected: ', options)

st.divider()

# st.slider()
values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
st.write('Values:', values)

appointment = st.slider(
    'Select your appointment',
    value=(time(11, 30), time(12, 45))
)
st.write('You are scheduled for:', appointment)

start_time = st.slider(
    'When do you start?',
    value=datetime(2020, 1, 1, 9, 30),
    format='MM/DD/YY - hh:mm'
)
st.write('Start time:', start_time)

st.divider()

# st.select_slider()
start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=['red', 'blue']
)
st.write('You selected wavelengths between', start_color, 'and', end_color)

st.divider()

# st.text_input()
title = st.text_input('Movie title', 'Life of Brian')
if title:
    st.write('The current movie title is ', title)