import streamlit as st
import pandas as pd
import numpy as np
import time
import altair as alt
import matplotlib.pyplot as plt
from datetime import datetime, date, time
from vega_datasets import data

source = data.cars()

chart = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin'
).interactive()

tab1, tab2 = st.tabs(['Streamlit theme (default)',
                      'Altair native theme'])

with tab1:
    st.altair_chart(chart, theme='streamlit', use_container_width=True)

with tab2:
    st.altair_chart(chart, theme=None, use_container_width=True)