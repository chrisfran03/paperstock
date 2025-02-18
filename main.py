from app.app import run
import streamlit as st
import pandas as pd
import numpy as np
import requests
from app.fetch_stocks.fetch_stocks import fetch_filtered_stocks
# if __name__ == "__main__":
#     run()

# st.title('Paperstock')
NASDAQ_URL = "https://api.nasdaq.com/api/quote/list-type/FIFTYTWOWEEKHILOW?&queryString=exchange%3Dq%7Cstatus%3DHi&limit=99999&sortColumn=symbol&sortOrder=ASC"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

st.sidebar.write("Options")
option = st.sidebar.selectbox(
    "Which Dashboard?", ('stocktwits', 'twitter', 'wallstreetbets', 'chart', 'pattern'))
st.header(option)

if option == 'twitter':
    st.subheader("twitter dashboard")

if option == 'chart':
    st.subheader("chart dashboard")

if option == 'stocktwits':
    # pass
    # try:
    #     response = requests.get(NASDAQ_URL, headers=headers)
    #     if response.status_code == 200:
    #         data = response.json()
    #         rows = data.get("data", {}).get("table", {}).get("rows", [])
    #         symbols = [
    #             stock['symbol']
    #             for stock in rows
    #             if float(stock['lastsale'].replace('$', '').replace(',', '')) >= 15
    #         ]
    #         st.write(symbols)
    # except requests.exceptions.RequestException as e:
    #     print(f"Request failed: {e}")
    st.write(fetch_filtered_stocks())
