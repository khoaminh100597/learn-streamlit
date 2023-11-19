import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date, time

# Create sample data
data_df = pd.DataFrame(
    {
        'widgets': ['st.select_box', 'st.number_input', 'st.text_area', 'st.text_button']
    }
)

data_num = pd.DataFrame(
    {
        'price':[20, 950, 250, 500]
    }
)

data_bool = pd.DataFrame(
    {
        'widgets': ['st.selectbox', 'st.number_input', 'st.text_area', 'st.button'],
        'favorite': [True, False, False, True]
    }
)

data_options = pd.DataFrame(
    {
        'category': [
            "📊 Data Exploration",
            "📈 Data Visualization",
            "🤖 LLM",
            "📊 Data Exploration"
            ]
    }
)

data_datetime = pd.DataFrame(
    {
        'appointment': [
            datetime(2024, 2, 5, 12, 30),
            datetime(2023, 11, 10, 18, 0),
            datetime(2024, 3, 11, 20, 10),
            datetime(2023, 9, 12, 3, 0),
        ]
    }
)

data_date = pd.DataFrame(
    {
        'birthday': [
            date(1980, 1, 1),
            date(1990, 5, 3),
            date(1974, 5, 19),
            date(2001, 8, 17)
        ]
    }
)

data_time = pd.DataFrame(
    {
        'appointment': [
            time(12, 30),
            time(18, 0),
            time(9, 10),
            time(16, 25)
        ]
    }
)

data_list = pd.DataFrame(
    {
        'sales': [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ]
    }
)

data_link = pd.DataFrame(
    {
        'apps': [
            "https://roadmap.streamlit.app",
            "https://extras.streamlit.app",
            "https://issues.streamlit.app",
            "https://30days.streamlit.app",
        ]
    }
)

data_images = pd.DataFrame(
    {
        'apps': [
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png",
        ]
    }
)

data_sales = pd.DataFrame({
    'sales': [200, 550, 1000, 80]
    }
)

# st.column_config.Column
st.data_editor(
    data_df,
    column_config={
        'widgets': st.column_config.Column(
            'Streamlit Widgets',
            help='Strealit **widget** commands',
            width='medium',
            required=True
        )
    },
    hide_index=True,
    num_rows='dynamic'
)

# st.column_config.TextColumn
st.data_editor(
    data_df,
    column_config={
        'widgets': st.column_config.TextColumn(
            'Widgets',
            help='Streamlit **widget** commands',
            width='medium',
            required=True,
            default='st.',
            max_chars=50,
            validate="^st\.[a-z_]+$"
        )
    },
    hide_index=True,
    num_rows='dynamic'
)

# st.column_config.NumberColumn
st.data_editor(
    data_num,
    column_config={
        'price': st.column_config.NumberColumn(
            'Price (in USD)',
            help='The price of the product in USD',
            min_value=0,
            max_value=1000,
            step=1,
            format='$%d'
        )
    },
    hide_index=True
)

# st.column_config.CheckboxColumn
st.data_editor(
    data_bool,
    column_config={
        'favorite': st.column_config.CheckboxColumn(
            'Your favorite?',
            help='Select your **favorite** widgets',
            default=False
        )
    },
    disabled=['widgets'],
    hide_index=True
)

# st.column_config.SelectboxColumn
st.data_editor(
    data_options,
    column_config={
        'category': st.column_config.SelectboxColumn(
            'App Category',
            help='The category of the app',
            width='medium',
            options=[
                "📊 Data Exploration",
                "📈 Data Visualization",
                "🤖 LLM"
            ],
            required=True
        )
    },
    hide_index=True
)

# st.column_config.DatetimeColumn
st.data_editor(
    data_datetime,
    column_config={
        'appointment': st.column_config.DateColumn(
            'Appointment',
            min_value=datetime(2023, 6, 1),
            max_value=datetime(2025, 1, 1),
            format='D MMM YYY, h:mm a',
            step=60
        )
    },
    hide_index=True
)

# st.column_config.DateColumn
st.data_editor(
    data_date,
    column_config={
        'birthday': st.column_config.DateColumn(
            'Birthday',
            min_value=date(1900, 1, 1),
            max_value=date(2005, 1, 1),
            format='DD.MM.YYYY',
            step=1
        )
    },
    hide_index=True
)

# st.column_config.TimeColumn
st.data_editor(
    data_time,
    column_config={
        'appointment': st.column_config.TimeColumn(
            'Appointment',
            min_value=time(8, 0, 0),
            max_value=time(19, 0, 0),
            format='hh:mm a',
            step=60
        )
    },
    hide_index=True
)

# st.column_config.ListColumn
st.data_editor(
    data_list,
    column_config={
        'sales': st.column_config.ListColumn(
            'Sales (last 6 months)',
            help='The sales volume in the last 6 months',
            width='medium'
        )
    },
    hide_index=True
)

# st.column_config.LinkColumn
st.data_editor(
    data_link,
    column_config={
        'apps': st.column_config.LinkColumn(
            'Trending apps',
            help='The top trending Streamlit apps',
            validate='^https://[a-z]+\.streamlit\.app$',
            max_chars=100
        )
    },
    hide_index=True
)

# st.column_config.ImageColumn
st.data_editor(
    data_images,
    column_config={
        'apps': st.column_config.ImageColumn(
            'Preview Image',
            help='Streamlit app preview screenshots'
        )
    },
    hide_index=True
)

# st.column_config.LineChartColumn
st.data_editor(
    data_list,
    column_config={
        'sales': st.column_config.LineChartColumn(
            'Sales (last 6 months)',
            width='medium',
            help='The sales volume in the last 6 months',
            y_min=0,
            y_max=100
        )
    },
    hide_index=True
)

# st.column_config.ProgressColumn
st.data_editor(
    data_sales,
    column_config={
        'sales': st.column_config.ProgressColumn(
            'Sales volume',
            help='The sales volume in USD',
            format='$%f',
            min_value=0,
            max_value=1000
        )
    },
    hide_index=True
)