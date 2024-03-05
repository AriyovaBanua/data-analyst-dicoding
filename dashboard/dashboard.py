import streamlit as st
import pandas as pd

# Load the dataset

def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/AriyovaBanua/data-analyst-dicoding/blob/c2c94a8f80f35f858da450b1102f2d06dff0767d/dashboard/hour.csv')

df = load_data()

# Title
st.title('Bike Sharing Data Analysis')

# Sidebar
st.sidebar.title('Filters')

# Map weather situation codes to their descriptions
weather_situations = {
    1: 'Clear, Few clouds, Partly cloudy, Partly cloudy',
    2: 'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist',
    3: 'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds',
    4: 'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog'
}

# Map season codes to their descriptions
seasons = {
    1: 'Spring',
    2: 'Summer',
    3: 'Fall',
    4: 'Winter'
}

# Select Season
season = st.sidebar.selectbox('Select Season', list(seasons.values()))

# Select Weather Situation
weather_situation_code = st.sidebar.selectbox('Select Weather Situation', list(weather_situations.values()))



# Filter the data
filtered_df = df[(df['season'] == list(seasons.keys())[list(seasons.values()).index(season)]) & 
                 (df['weathersit'] == list( weather_situations.keys())[list( weather_situations.values()).index(weather_situation_code)])]
list( weather_situations.keys())[list( weather_situations.values()).index(weather_situation_code)]

# Show the filtered data
st.write(filtered_df)

# Data Visualization
st.subheader('Data Visualization')

st.write('Bike Rental Counts by Hour')
# Line Chart of Rental Counts by Hour
hourly_rentals = filtered_df.groupby('hr')['cnt'].sum()
st.line_chart(hourly_rentals)

st.write('Bar Chart of Rental Counts by Weekday')
# Bar Chart of Rental Counts by Weekday
weekday_rentals = filtered_df.groupby('weekday')['cnt'].sum()
st.bar_chart(weekday_rentals)
