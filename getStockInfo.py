# Type 'pip install yfinance' before running
import yfinance as yf
import pandas as pd

# Holds list of all Stock Tickers
tickers_list = ['aapl', 'ebay', 'nue', 'f', 'tme', 'twtr', 'rblx', 'pfe', 't', 'wfc', 'msft', 'intc', 'tsla', 'pypl', 'hood', 'dis']
tickers = yf.Tickers(tickers_list)

# Download all list of Tickers
df = tickers.download(group_by='tickers')

# Prints EBAY Info
print(df['EBAY'])