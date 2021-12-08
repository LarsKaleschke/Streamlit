import streamlit as st
import pandas as pd
import numpy as np

st.title('Sea ice test')

DATE_COLUMN = 'Date'

DATA_URL = ('https://www.seaice.de/nh_awi_amsr2_regional_extent_area.csv')



@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done! (using st.cache)")

st.subheader('Raw data')
st.write(data)

