# Type 'pip install yfinance' before running
import yfinance as yf
import pandas as pd

shortTermTrend = [] # List that Compares Present Day Stock Price to Previous Day's Stock Price

midTermTrend = [] # List that Compares Present Day Stock Price to Previous Month's Stock Price

# Holds list of all Stock Tickers

tickers_list = ['aapl', 'ebay', 'nue', 'f', 'tme', 'twtr', 'rblx', 'pfe', 't', 'wfc', 'msft', 'intc', 'tsla', 'pypl', 'hood', 'dis']
tickers = yf.Tickers(tickers_list)

# Download all list of Tickers
df = tickers.download(group_by='tickers')

# Prints EBAY Info
print(df['EBAY'])

# Converts to uppercase
tickers_list = [x.upper() for x in tickers_list]


for x in tickers_list:
    shortchang = ((df[x]['Close'][0]) - (df[x]['Close'][1])) # Contains Change of Stock from Previous Day
    # Puts Variables into List
    shortTermTrend.append(
        {
            'Ticker': x,
            'Change': shortchang
        }
    )
    
    midchang = ((df[x]['Close'][0]) - (df[x]['Close'][22])) # Contains Change of Stock from Previous Month
    # Puts Variables into List
    midTermTrend.append(
        {
            'Ticker': x,
            'Change': midchang
        }
    )

shortTermTrend = pd.DataFrame(shortTermTrend) # Turns List to Dataframe
#print(shortTermTrend.sort_values(by='Change', ascending=False))

midTermTrend = pd.DataFrame(midTermTrend) # Turns List to Dataframe
#print(midTermTrend.sort_values(by='Change', ascending=False))