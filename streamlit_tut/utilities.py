import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title='Ex-streaml-ly Cool App',
    page_icon='🧊',
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
def get_user_name():
    return 'Minh'

with st.echo():
    def get_punctuation():
        return '!!!'
    
    st.write('This code will be printed')
    greeting = 'Hi there'
    punctuation = get_punctuation()
    st.write(greeting, get_user_name(), punctuation)

# st.help(pd.DataFrame)
st.write('Done!')
st.write(st.experimental_get_query_params())
st.experimental_set_query_params(
    show_map=True,
    selected=["asia", "america"],
)