from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# Importing the StringIO module.
from io import StringIO 
import nltk
from nltk import ngrams
from collections import Counter
import seaborn as sns
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

st.header("Barcelona Rent Prices - 'Choose an affordable-safe neighbourhood at your preferred place'")

data = pd.read_csv("data/Barcelona_rent_price.csv")

df_year = data.groupby(['Year'])['Price'].mean().reset_index(name='average price')

line = alt.Chart(df_year,title = "Rent over the years in Barcelona").mark_line().encode(
    x='Year:N',
    y=alt.Y('average price',
    scale =alt.Scale(zero=False))
)
st.altair_chart(line.interactive(), use_container_width=True)

dataframe1  = data[data['Average _rent']== 'average rent (euro/month)']
dataframe2  = data[data['Average _rent']== 'average rent per surface (euro/m2)']

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

st.write('The average price of rental housing in Barcelona reached 17.6 euros per square metre in the first quarter of 2020, well above the Spanish average of 10.2 euros per square metre')
