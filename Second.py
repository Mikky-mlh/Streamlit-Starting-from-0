import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""

# Simple Stock Price app

Stock closing price and volume of Google

""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerOf = tickerData.history(start="2010-5-31", end="2020-5-31")

st.line_chart(tickerOf.Close)
st.line_chart(tickerOf.Volume)