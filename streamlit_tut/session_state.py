import streamlit as st

def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)
    
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

st.text_input('Your name', key='name')
st.write('Your name is', st.session_state.name)

