# Import required libraries
import yfinance as yf  # For fetching stock data
import streamlit as st  # For creating web app
import pandas as pd  # For data manipulation

# Display app title and description
st.write("""

# Simple Stock Price app

Stock closing price and volume of Google

""")

# Define the stock ticker symbol
tickerSymbol = 'GOOGL'

# Create a ticker object for the specified stock
tickerData = yf.Ticker(tickerSymbol)

# Fetch historical stock data between specified dates
tickerOf = tickerData.history(start="2010-5-31", end="2020-5-31")

# Display closing price as a line chart
st.line_chart(tickerOf.Close)
# Display trading volume as a line chart
st.line_chart(tickerOf.Volume)