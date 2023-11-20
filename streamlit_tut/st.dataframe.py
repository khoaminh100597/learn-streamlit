import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.rand(50, 20),
    columns=['col %d' % i for i in range(1, 21)]
)

# st.dataframe()
st.dataframe(df)

# change the style
st.dataframe(df.style.highlight_max(axis=0))

# customize the dataframe via column_config, hide_index, column_order
df = pd.DataFrame(
    {
        'name': ['Roadmap', 'Extrax', 'Issues'],
        'url': ['https://roadmap.streamlit.app',
                'https://extras.streamlit.app',
                'https://issues.streamlit.app'],
        'stars': [np.random.randint(0, 1000) for _ in range(3)],
        'views_history': [[np.random.randint(0, 5000)
                           for _ in range(30)] for _ in range(3)]
    }
)

st.checkbox('Use container width',
            value=False,
            key='use_container_width')

st.dataframe(
    df,
    column_config={
        'name': 'App name',
        'stars': st.column_config.NumberColumn(
            'Github Stars',
            help='Number of stars on Github',
            format='%d ⭐'
        ),
        'url': st.column_config.LinkColumn('App URL'),
        'views_history': st.column_config.LineChartColumn(
            'Views',
            y_min=0,
            y_max=5000
        )
    },
    hide_index=True,
    use_container_width=st.session_state.use_container_width
)