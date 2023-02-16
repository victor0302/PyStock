import pandas as pd
from src.alpha_vantage_api import get_stock_data



symbol = "NVDA"
interval = "daily"
api_key = "3W0BP65OHZVWR6EX"

# Get stock data using API call
df = get_stock_data(symbol, interval, api_key)

# Convert data strings to datetime objects and set as index
df.index = pd.to_datetime(df.index)

# Filter data to last year
last_year = df.index >= pd.Timestamp('today') - pd.DateOffset(years=1)
df = df.loc[last_year]

# Resample data to weekly intervals and aggregate using different summary statistics
weekly_df = df.resample('W').agg({
    '1. open': 'first',
    '2. high': 'max',
    '3. low': 'min',
    '4. close': 'last',
    '5. adjusted close': 'last',
    '6. volume': 'sum',
    '7. dividend amount': 'sum',
    '8. split coefficient': 'last'
})
# 10 day moving average of the closing price
weekly_df['10-day MA'] = weekly_df['4. close'].rolling(window=10).mean()



