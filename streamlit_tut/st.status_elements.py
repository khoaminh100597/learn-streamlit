import streamlit as st
import pandas as pd
import numpy as np
import time

progress_text = 'Operation in progress. Please wait.'

# st.progress()
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)

# st.spinner()
with st.spinner('Wait for it...'):
    time.sleep(5)

# st.status()
with st.status('Downloading data...', expanded=True) as status:
    st.write('Searching for data...')
    time.sleep(2)
    st.write('Found URL')
    time.sleep(1)
    st.write('Downloading data...')
    time.sleep(1)
    status.update(label='Download complete!', state='complete', expanded=False)

# st.toast()
if st.button('Three toasts'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')

# st.balloons()
st.balloons()

# st.snow()
st.snow()

# st.error()
st.error('Error message')

# st.info()
st.info('Info message')

# st.success()
st.success('Done')

# st.exception()
st.exception(Exception('New exception'))
st.button('Rerun')