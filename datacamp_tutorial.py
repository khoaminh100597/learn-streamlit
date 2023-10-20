import time
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt
import graphviz

# How to run your Streamlit code
# streamlit run file_name.py

# Displays texts with Streamlit
# st.write("Hello, let's learn how to build a streamlit app together")
# st.title('This is a title')
# st.header('This is a header')
# st.subheader('This is a subheader')
# st.caption('This is a caption')
# st.code('print("hello")')
# st.latex(r''' a+a r^1+a r^2+a r^3 + exp(5) ''')

# Display an image, video, or audio file with Streamlit
# st.image(rf'.\examples\doraemon.png')
# st.video(rf'.\examples\earth.mp4')
# st.audio(rf'.\examples\boom.mp3')

# Input Widgets
# st.checkbox('yes') # This function returs a Boolean value. When the box is checked, it returns a True value, otherwise a False value
# st.button('Click')
# st.radio('Pick your gender', ['Male', 'Female'])
# st.selectbox('Pick your gender',['Male','Female'])
# st.multiselect('Choose a planet', ['Mars', 'Jupyter', 'Neptune'])
# st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
# st.slider('Pick a number', 0)

# st.number_input('Pick a number', 0, 10)
# st.text_input('Email address')
# st.date_input('Travelling date')
# st.time_input('School time')
# st.text_area('Description')
# st.file_uploader('Upload a photo')
# st.color_picker('Choose your favorite color')

# Display progress and status with Streamlit
# st.balloons() # This function is used to display ballons for celebration
# st.progress(10) # This function is used to display a progress bar
# with st.spinner('Wait for it ...'): # This function is used to display a temporary waiting mesage during execution
#     time.sleep(2)
#     st.write('Well done')

# st.success('You did it!')
# st.error('Error')
# st.info('It is easy to build a streamlit app')
# st.exception(RuntimeError('RuntimeError Exception'))
# st.warning('Warning')

# Sidebar: passing an element to st.sidebar() will make this element pinned to the left
# but st.spinner() and st.echo() are not supported with st.sidebar
# st.sidebar.title('This is written inside the sidebar')
# st.sidebar.button('Click')
# st.sidebar.radio('Pick your gender', ['Male', 'Female'])

# Container: is used to create an invisible container where you can put elements in order to create a useful arrangement and hierarchy
# container = st.container()
# container.write('This is written inside the container')
# st.write('This is written outside the container')

# Display graphs with Streamlit

# This function is used to display a matplotlib.pyplot figure
# rand = np.random.normal(1, 2, size=20)
# fig, ax = plt.subplots()
# ax.hist(rand, bins=15)
# st.pyplot(fig)

# This function is used to display a line chart
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)

# This function is used to display a bar chart
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.bar_chart(df)

# This function is used to display an area chart
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.area_chart(df)

# This function is used to display an altair chart
df = pd.DataFrame(np.random.randn(500, 3), columns=['x', 'y', 'z'])
c = alt.Chart(df).mark_circle().encode(x='x' , y='y' , size='z', color='z', tooltip=['x', 'y', 'z'])
st.altair_chart(c, use_container_width=True)

# This function is used to display graph objects, which can be completed using different nodes and edges
st.graphviz_chart('''    digraph {        Big_shark -> Tuna        Tuna -> Mackerel        Mackerel -> Small_fishes        Small_fishes -> Shrimp    }''')

# Display maps
df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
st.map(df)