import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    [
        ['st.selectbox', 4, True],
        ['st.balloons', 5, False],
        ['st.time_input', 3, True]
    ],
    columns=[
        'command',
        'rating',
        'is_widget'
    ]
)

edited_df = st.data_editor(df, num_rows='dynamic')
favorite_command = edited_df.loc[edited_df['rating'].idxmax()]['command']
st.markdown(f'Your favorite command is **{favorite_command}**')

edited_df = st.data_editor(
    df,
    column_config={
        'command': 'Streamlit command',
        'rating': st.column_config.NumberColumn(
            'Your rating',
            help='How much do you like this command (1-5)?',
            min_value=1,
            max_value=5,
            step=1,
            format='%d ⭐'
        ),
        'is_widget': 'Widget ?'
    },
    disabled=['command', 'is_widget'],
    hide_index=True
)
favorite_command = edited_df.loc[edited_df['rating'].idxmax()]['command']
st.markdown(f'Your favorite command is **{favorite_command}**')
