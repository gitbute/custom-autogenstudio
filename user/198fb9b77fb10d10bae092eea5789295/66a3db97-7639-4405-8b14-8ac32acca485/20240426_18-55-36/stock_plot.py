# filename: stock_plot.py

import yfinance as yf
import matplotlib.pyplot as plt

# Download the stock data for 2023
nvda_data = yf.download('NVDA', start='2023-01-01', end='2023-12-31')
tesla_data = yf.download('TSLA', start='2023-01-01', end='2023-12-31')

# Plot the stock prices
plt.plot(nvda_data.index, nvda_data['Close'], label='NVDA')
plt.plot(tesla_data.index, tesla_data['Close'], label='TSLA')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('NVDA and TSLA Stock Price for 2023')
plt.legend()
plt.savefig('nvda_tesla.png')
plt.show()