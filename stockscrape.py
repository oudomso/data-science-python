import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import date

st.write("""
### Simple stock price app

shown are the stock closing price and volume of stock


""")


tickerSymbol = input("Enter Ticker symbol")

tickerData.yf.Ticker(tickerSymbol)

currentdate = today.strftime("%Y-%m-%d")

tickerDf = tickerData.history(period='1d', start="2000-1-1", end=currentdate)


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)