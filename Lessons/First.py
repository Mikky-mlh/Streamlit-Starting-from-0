import streamlit as st
import pandas as pd

# importing libraries pandas for graph and streamlit for frontend

st.title("First Streamlit App") #title
st.write("Hello World") # text
st.write("Hello Again")

df = pd.read_csv("my_data.csv")
st.line_chart(df) # gives line chart

number = st.slider("Pick a number", 0, 100) #widget for slider

date = st.date_input("Pick a date") # widget for date

st.bar_chart(df, x="Month", y="Sales") # gives bar chart

pets = ["Cat", "Dog", "Bird"] 
pet = st.radio("Pick a pet", pets) # radio: choose one option