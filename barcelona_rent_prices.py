
import numpy as np
import pandas as pd

import streamlit as st

import altair as alt


st.header("Rent Prices in Barcelona  - 'Choose an affordable neighbourhood at your preferred place'")

data = pd.read_csv("data/Barcelona_rent_price.csv")

dataframe1  = data[data['Average _rent']== 'average rent (euro/month)']
dataframe2  = data[data['Average _rent']== 'average rent per surface (euro/m2)']

rent_metrics = ['average rent (euro/month)','average rent per surface (euro/m2)']

rent_metric = st.sidebar.selectbox(
            'Choose the average rent metric',
            rent_metrics)

if rent_metric == 'average rent (euro/month)':
    data = dataframe1
else:
    data = dataframe2

df_year = data.groupby(['Year'])['Price'].mean().reset_index(name='average price')

st.write('The average price of rental housing in Barcelona seems to follow the same trend when metric is considered "euro/m2" or "euro/month"')

st.write('This trend reached 13.4 euros per square metre in the first quarter of 2022, well above the Spanish average of 10.2 euros per square metre. On a monthly basis, average rent reached 920 where the spanish average lies under 870')

st.write("A downward trend is seen between 2019 and 2021, falling from 13.4 to a minimum of 12.7 euros per square meter during that period. It was not until 2017 when the level price recovered to the figures of before the financial crisis and the bursting of the real state bubble. From then onwards, rental property prices soared and reached their highest point in 2020 with 13.4 euros per square meter.")

line = alt.Chart(df_year,title = f"Rent over the years in Barcelona in {rent_metric}").mark_line().encode(
    x='Year:N',
    y=alt.Y('average price',
    scale =alt.Scale(zero=False))
)
st.altair_chart(line.interactive(), use_container_width=True)

col1,col2 = st.columns(2)
hist = alt.Chart(dataframe1,title = "Histogram of Prices(average rent (euro/month))").mark_bar().encode(
    alt.X("Price:Q", bin=True),
    y='count()',
)
col1.altair_chart(hist, use_container_width = True)


hist1 = alt.Chart(dataframe2,title = "Histogram of Prices(average rent per surface (euro/m2))").mark_bar().encode(
    alt.X("Price:Q", bin=True),
    y='count()',
)
col2.altair_chart(hist1, use_container_width = True)
