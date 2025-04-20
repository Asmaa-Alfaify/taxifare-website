import streamlit as st
import requests
from datetime import datetime

st.title('Taxi Fare preidictor')


st.markdown('select ride details below')


pickup_data = st.date_input('pickup_data',value= datetime.today())
pickup_time = st.time_input('pickup_time',value= datetime.now().time())
pickup_datetime = f"{pickup_data} {pickup_time}"
pickup_longitude = st.number_input('pickup longitude', value=-73.985)
pickup_latitude = st.number_input('pickup latitude', value=40.748)
dropoff_longitude = st.number_input('dropoff longitude', value=40.748)
dropoff_latitude = st.number_input('dropoff latitude', value=40.748)
passenger_count = st.slider('passenger count', min_value=1, max_value=8, value=1)


url = 'https://taxifare.lewagon.ai/predict'

if st.button('Get Fare Estimate'):
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        prediction = response.json().get('fare', 'Error: no fare returned')
        st.success(f"Estimated fare: ${prediction:.2f}")
    else:
        st.error(f"API error: {response.status_code}")
