import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.figure_factory as ff
import graphviz
from vega_datasets import data
from bokeh.plotting import figure

# st.area_chart()
chart_data = pd.DataFrame(np.random.randn(20, 3),
                          columns=['a', 'b', 'c'])
st.area_chart(chart_data)

# st.bar_chart()
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.bar_chart(chart_data)

# st.line_chart()
chart_data = pd.DataFrame(np.random.randn(20, 3),
                          columns=['a', 'b', 'c'])
st.line_chart(chart_data)

# st.scatter_chart()
st.scatter_chart(chart_data)

# st.pyplot()
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)

# st.altair_chart()
c = (
    alt.Chart(chart_data).mark_circle().encode(x='a',
                                               y='b',
                                               size='c',
                                               color='c',
                                               tooltip=['a', 'b', 'c'])
)
st.altair_chart(c, use_container_width=True)

# st.altair_chart()
source = data.cars()
chart = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin'
).interactive()
tab1, tab2 = st.tabs(
    ['Streamlit theme (default)',
     ('Altair native theme')]
)
with tab1:
    # Use the Streamlit theme
    # This is the default
    st.altair_chart(chart, theme='streamlit', use_container_width=True)
with tab2:
    # Use the Altair theme
    st.altair_chart(chart, theme=None, use_container_width=True)

# st.vega_lite_chart()
chart = {
    "mark": "point",
    "encoding": {
        "x": {
            "field": "Horsepower",
            "type": "quantitative",
        },
        "y": {
            "field": "Miles_per_Gallon",
            "type": "quantitative",
        },
        "color": {"field": "Origin", "type": "nominal"},
        "shape": {"field": "Origin", "type": "nominal"},
    },
}

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Vega-Lite native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.vega_lite_chart(
        source, chart, theme="streamlit", use_container_width=True
    )
with tab2:
    st.vega_lite_chart(
        source, chart, theme=None, use_container_width=True
    )

# st.plotly_chart()
# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

# st.bokeh_chart()
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)

# st.graphviz_chart()
graph = graphviz.Digraph()
graph.edge('run', 'intr')
graph.edge('intr', 'runbl')
graph.edge('runbl', 'run')
graph.edge('run', 'kernel')
graph.edge('kernel', 'zombie')
graph.edge('kernel', 'sleep')
graph.edge('kernel', 'runmem')
graph.edge('sleep', 'swap')
graph.edge('swap', 'runswap')
graph.edge('runswap', 'new')
graph.edge('runswap', 'runmem')
graph.edge('new', 'runmem')
graph.edge('sleep', 'runmem')

st.graphviz_chart(graph)

# st.map()
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(df)
