# This file contains the function to make an API call to Alpha Vantage to retrieve stock data
import requests
import pandas as pd


# Define function to get stock data from Alpha Vantage API
def get_stock_data(symbol, interval, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&interval={interval}&apikey={api_key}"
    # API request and response
    response = requests.get(url)
    data = response.json()["Time Series (Daily)"]
    df = pd.DataFrame(data).transpose()
    return df
