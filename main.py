import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the next Days")
place = st.text_input("Place: ")
days = st.slider('Forecast Days', min_value=1, max_value=5,
                  help="Select the number of forecasted days")
option = st.selectbox("Slect data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["14-04-2023", "15-04-2023", "16-04-2023"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (c)"})
st.plotly_chart(figure)