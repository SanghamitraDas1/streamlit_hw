import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
from vega_datasets import data

df = pd.read_csv('Videogame_Sales.csv')

st.sidebar.header("Select the Platform and Region")
x_val = st.sidebar.multiselect("Pick your Platforms",df['Platform'])
all_platforms = st.sidebar.checkbox("Select all platforms")
if all_platforms:
     x_val = df['Platform']
platform_df = df[df['Platform'].isin(x_val)]
y_val = st.sidebar.selectbox("Pick your Region",platform_df.select_dtypes(include=np.number).columns.tolist())

st.title("Videogame Console Sales")
chart_data = alt.Chart(platform_df).mark_bar().encode(
                 x = alt.X('Platform', sort=alt.EncodingSortField(field="Platform", op="count", order='descending')),
                 y = y_val)
st.altair_chart(chart_data, use_container_width=True)
