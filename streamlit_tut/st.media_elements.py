import streamlit as st
from PIL import Image

image = Image.open('./streamlit_tut/sample_image.jpg')
st.image(image)

audio_file = open('./streamlit_tut/piano.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes)

video_file = open('./streamlit_tut/video.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)