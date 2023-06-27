import streamlit as st
import plotly.express as px
from backend import get_data

st.title("weather forecast for next days".capitalize())

lat, lon = st.text_input("place: lat: "),st.text_input("place: lon: ")

days = st.slider("Forecast days", min_value=1, max_value=5, help="Select number for days to forecast")



option = st.selectbox("select data to view",("temprature","sky"))
st.subheader(f"{option} for next {days} in place of {lat},{lon}")

# def get_data(days):

#     dates = ["2022-09-22","2022-09-23","2022-09-24"]
#     temprature = [10,11,15]
#     temprature = [days*i for i in temprature]
#     return dates,temprature
# dates, temprature = get_data(days)



if lat and lon:
    filtered_data = get_data(lat,lon,days)

    if option =="temprature":
        temprature = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temprature , labels={"x":"Date","y":"temprature"})
        st.plotly_chart(figure)

    if option =="sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
        image = f"images/{filtered_data}.png"
        st.image(image)