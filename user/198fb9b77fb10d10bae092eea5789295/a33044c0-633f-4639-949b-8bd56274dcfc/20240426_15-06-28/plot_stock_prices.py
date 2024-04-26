# filename: plot_stock_prices.py
import pandas as pd
import matplotlib.pyplot as plt

# Download stock prices from Yahoo Finance API
nvda_data = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/NVDA?period1=1672512000&period2=1675097600&interval=1d&events=history&includeAdjustedClose=true', parse_dates=['Date'], index_col='Date')
tesla_data = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/TSLA?period1=1672512000&period2=1675097600&interval=1d&events=history&includeAdjustedClose=true', parse_dates=['Date'], index_col='Date')

# Plot stock prices
nvda_tesla_data = pd.concat([nvda_data, tesla_data], axis=1)
nvda_tesla_data.columns = ['NVDA', 'TSLA']
plt.figure(figsize=(10, 6))
plt.plot(nvda_tesla_data.index, nvda_tesla_data['NVDA'], label='NVDA')
plt.plot(nvda_tesla_data.index, nvda_tesla_data['TSLA'], label='TESLA')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('NVDA and TESLA Stock Prices for 2023')
plt.legend()
plt.savefig('nvda_tesla.png')
