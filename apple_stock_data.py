import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("""
    # Приложение по котировке акций
        
    Отражает данные о котировках компании ***Apple*** за последние 5 лет 
         
         """ )
tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='5y', start='2018-10-15', end='2023-10-15')

# Создайте график цен закрытия (Close)
st.write("## График цен закрытия")
st.line_chart(tickerDf.Close, use_container_width=True)
st.write("Подпись оси X: Дата")
st.write("Подпись оси Y: Цена закрытия, $")

# Создайте график объема (Volume)
st.write("## График объема")
st.line_chart(tickerDf.Volume, use_container_width=True)
st.write("Подпись оси X: Дата")
st.write("Подпись оси Y: Объем")