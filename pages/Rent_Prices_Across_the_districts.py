
import numpy as np
import pandas as pd

import streamlit as st

import altair as alt


data = pd.read_csv("data/Barcelona_rent_price.csv")

#df_year = data.groupby(['Year'])['Price'].mean().reset_index(name='average price')

rent_metrics = ['average rent (euro/month)','average rent per surface (euro/m2)']

rent_metric = st.sidebar.selectbox(
            'Choose the average rent metric',
            rent_metrics)

dataframe1  = data[data['Average _rent']== 'average rent (euro/month)']
dataframe2  = data[data['Average _rent']== 'average rent per surface (euro/m2)']

if rent_metric == 'average rent (euro/month)':
    data = dataframe1
else:
    data = dataframe2 
#to be asked by Chase
st.header(f'Rent prices in selected districts based on {rent_metric} are shown in the below plots' )

tab1,tab2,tab3 = st.tabs(['Year Data', 'Trimester Data' , 'Districts and Neighbourhood Data'])

with tab1:
    years_list = [2014,2015,2016,2017,2018,2019,2020,2021,2022]
    years = st.multiselect(
            'Choose years',
            years_list)

    if not years:
        st.write('please select a year/years to view the yearly data')
    else:
        df_years = data.loc[data['Year'].isin(years)]
        st.write(df_years.head())

        district_data = df_years.groupby(['District'])['Price'].max().reset_index(name='district_max_price').sort_values(['district_max_price'],ascending = False)
        neighbours_data = df_years.groupby(['Neighbourhood'])['Price'].max().reset_index(name='neighbourhood_max_price').sort_values(['neighbourhood_max_price'],ascending = False)
        costliest_districts = district_data.head(3)
        cheapest_districts = district_data.tail(3)
        
        costliest_neighbourhood = neighbours_data.head(3)
        cheapest_neighbourhood = neighbours_data.tail(3)
        
        

        st.subheader('Costliest and Cheapest Districts over the years %s are shown below' % years)
        
        bar = alt.Chart(district_data,title = "Districts Bar Graph - Costliest to Cheapest").mark_bar().encode(
            alt.Y("district_max_price:Q"),
            x=alt.X('District',sort='-y')
        )

        st.altair_chart(bar, use_container_width=True)

        col1,col2 = st.columns(2)
        col1.subheader('Top 3 Costliest Districts')
        col1.write(costliest_districts)
        col2.subheader('Bottom 3 Cheapest Districts')
        col2.write(cheapest_districts)
        
        st.subheader('Costliest and Cheapest Neighbourhoods over the years %s are shown below' % years)
        
        bar = alt.Chart(neighbours_data,title = "Districts Bar Graph - Costliest to Cheapest").mark_bar().encode(
            alt.X("neighbourhood_max_price:Q"),
            y=alt.Y('Neighbourhood',sort='-x')
        )

        st.altair_chart(bar, use_container_width=True)

        col1,col2 = st.columns(2)
        col1.subheader('Top 3 Costliest Neighbourhood')
        col1.write(costliest_neighbourhood)
        col2.subheader('Bottom 3 Cheapest Neighbourhood')
        col2.write(cheapest_neighbourhood)
        st.write('Note : Costliest/Cheapest neighbourhood may or may be in the respective costliest/cheapest district')
with tab2:
    trimester_list = [1,2,3]
    trimester = st.multiselect(
     'Select the trimesters',
     trimester_list)
    if not trimester:
        st.write('please select a trimester')
    else:
        df_trimester = data.loc[data['Trimester'].isin(trimester)]
        st.write(df_trimester.head())
        df_trimester = df_trimester.groupby(['Year','Trimester'])['Price'].mean().reset_index(name='Average_Rent')
        trimester_line_plot = alt.Chart(df_trimester,title = f"Rent over the years based on selected trimesters").mark_line().encode(
            x='Year:N',
            y=alt.Y('Average_Rent',
            scale =alt.Scale(zero=False)),
            color='Trimester',
            strokeDash='Trimester',
            )
        st.altair_chart(trimester_line_plot.interactive(), use_container_width=True)
        
with tab3:
    col1,col2 = st.columns(2)

    with col1:
        
        district_list = data['District'].unique()
        districts = st.multiselect(
                'Choose a district',
                district_list)

    if not districts:
        st.write('please select a District to view its data')
    else:
        with col2:
            df_district = data.loc[data['District'].isin(districts)]
            neighbourhood = st.multiselect(
                'Choose a Neighbourhood',
            df_district['Neighbourhood'])
            if not neighbourhood : 
                st.write('please select a District to view its data')

        df_Neighbourhood = df_district.groupby(['Year','Neighbourhood'])['Price'].mean().reset_index(name='neighbourhood_avg_price')

        df_Neighbourhood = df_Neighbourhood.loc[df_Neighbourhood['Neighbourhood'].isin(neighbourhood)]

        st.write(df_district.head(3))

        df_district = df_district.groupby(['Year','District'])['Price'].mean().reset_index(name='district_avg_price')

        ml = alt.Chart(df_district,title = f"Rent over the years based on selected districts").mark_line().encode(
            x='Year:N',
            y=alt.Y('district_avg_price',
            scale =alt.Scale(zero=False)),
            color='District',
            strokeDash='District',
            )

        st.altair_chart(ml.interactive(), use_container_width=True)

        ml1 = alt.Chart(df_Neighbourhood,title = f"Rent over the years based on selected Neighbourhoods").mark_line().encode(
            x='Year:N',
            y=alt.Y('neighbourhood_avg_price',
            scale =alt.Scale(zero=False)),
            color='Neighbourhood',
            strokeDash='Neighbourhood',
            )

        st.altair_chart(ml1.interactive(), use_container_width=True)


