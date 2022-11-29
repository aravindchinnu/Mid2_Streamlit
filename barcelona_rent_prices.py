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

st.header("Barcelon Rent Prices")

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 ❄️")
    st.sidebar.markdown("# Page 3 ❄️")

data = pd.read_csv("data/Barcelona_rent_price.csv")

df_year = data.groupby(['Year'])['Price'].mean().reset_index(name='average price')

line = alt.Chart(df_year,title = "Rent Price per month in Barcelona").mark_line().encode(
    x='Year',
    y='average price'
)
st.altair_chart(line.interactive(), use_container_width=True)
#st.line_chart(df_year)

years_list = [2014,2015,2016,2017,2018,2019,2020,2021,2022]
trimester_list = [1,2,3]

district_list = data['District'].unique()

years = st.sidebar.multiselect(
            'Choose a year',
            years_list)

districts = st.sidebar.multiselect(
            'Choose a district',
            district_list)
df4 = data.groupby(['District','Neighbourhood'])['Price'].mean().reset_index(name='average price')
if districts:
    df5 = df4.loc[df4['District'].isin(districts)]
    neighbourhood = st.sidebar.multiselect(
            'Choose a Neighbourhood',
            df5['Neighbourhood'])
trimester = st.sidebar.multiselect(
     'Select the trimester',
     trimester_list)
     
col1,col2 = st.columns(2)