# Type 'pip install yfinance' before running
from matplotlib import pyplot as plt
import yfinance as yf
import pandas as pd

# TODO: this has to be within a function so that it can be called in the bussiness logic

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
    
    # TODO: I changed this cause it wasn't working
    midchang = ((df[x]['Close'][0]) - (df[x]['Close'][1])) # Contains Change of Stock from Previous Month
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

def generate_graph(tick: str):
    # forces it to capitlize
    tick = tick.upper();

    # checks if its in the list
    if(tick in tickers_list):
        print("showing tick")
        print(df[tick])
        sub = yf.Ticker(tick).history(period = '1y') # grabs the sub item
        plt.clf()
        plt.plot(sub.index, sub['Close'])
        plt.ylabel('Dollars')
        plt.xlabel('Date')
        try:
            plt.title(yf.Ticker(tick).info['longName'] + "(" + tick +")")
        except:
            print("no value in chosen_stock")
        # TODO:decide where it will save
        plt.savefig(f"FrontEnd/BAWS/static/{tick}.png"); # saves the figure
    else:
        sub = yf.Ticker(tick).history(period = '1y') # grabs the sub item
        plt.clf()
        plt.plot(sub.index, sub['Close'])
        plt.ylabel('Dollars')
        plt.xlabel('Date')
        try:
            plt.title(yf.Ticker(tick).info['longName'] + "(" + tick +")")
        except:
            print("no value in chosen_stock")
        # TODO:decide where it will save
        plt.savefig(f"FrontEnd/BAWS/static/{tick}.png"); # saves the figure
