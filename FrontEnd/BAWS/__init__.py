import imp
from flask import Flask, render_template, request, Blueprint, redirect, url_for
import pandas as pd
from os import path
import yfinance as yf
import random
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from BAWS import getStockInfo
import time
app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def getLoginData():
    if request.method == 'POST':
        USERNAME = str(request.form['UsernameL'])
        PASSWORD = str(request.form['PasswordL'])
        user_table = pd.read_csv('FrontEnd/BAWS/FileStorage/user.csv')
        if USERNAME in user_table["Username"].values and PASSWORD in user_table["Password"].values:
            return redirect(url_for('views.index'))
        print(user_table, file = sys.stderr)
    
    return render_template("loginPage.html")


@app.route('/index', methods=['GET', 'POST'])
def home():
    #ticker_list gives the list of stocks 
    tickers_list = ['AAPL', 'EBAY', 'NUE', 'F', 'TME', 'TWTR', 'RBLX', 'PFE', 'T', 'WFC', 'MSFT', 'INTC', 'TSLA', 'PYPL', 'HOOD', 'DIS']
    
    # List that Compares Present Day Stock Price to Previous Day's Stock Price
    shortTermTrend = []
    
    # List that Compares Present Day Stock Price to Last Month's Stock Price
    longTermTrend = [] 
    
    # List of Stocks to Display
    display_list = []
    
    number_array = [0,1,2,3,4,5,6,7,8,9]
    
    #searches yahoo finance for tickers from the ticker_list
    tickers = yf.Tickers(tickers_list)
    #prints the list of tickers from tickers
    print(tickers, file =sys.stderr) 
    
    #downloads everything to do with tickers into the code so that we can use it
    df = tickers.download(group_by='ticker')
    
    for x in tickers_list:
        shortchang = ((df[x]['Close'][19]) - (df[x]['Close'][18])) # Contains Change of Stock from Previous Day
        # Puts Variables into List
        shortTermTrend.append(
            {
                'Ticker': x,
                'Change': shortchang
            }
        )
    
    # Creates Dataframe
    shortTermTrend = pd.DataFrame(shortTermTrend)
    # Sort values from highest to lowest
    shortTermTrend = shortTermTrend.sort_values(by='Change', ascending=False)
    # Changes index to reflex sorted values
    shortTermTrend = shortTermTrend.reset_index(drop=True)
    
    for x in tickers_list:
        longchang = ((df[x]['Close'][19]) - (df[x]['Close'][0])) # Contains Change of Stock from Previous Month
        # Puts Variables into List
        longTermTrend.append(
            {
                'Ticker': x,
                'Change': longchang
            }
        )
    
    # Creates Dataframe
    longTermTrend = pd.DataFrame(longTermTrend)
    # Sort values from highest to lowest
    longTermTrend = longTermTrend.sort_values(by='Change', ascending=False)
    # Changes index to reflex sorted values
    longTermTrend = longTermTrend.reset_index(drop=True)
    
    # Displays Random set of Stocks
    display_list = random.sample(tickers_list, 10)
    
    if request.method == 'POST': 

        if request.form.get('test1'):
            # Activate Test 1
            print(shortTermTrend)

            for y in number_array:
                display_list[y] = shortTermTrend['Ticker'][y]
        
        if request.form.get('test2'):
            # Activate Test 2
            print('Test 2 Activated')
            print(longTermTrend)
            
            for y in number_array:
                display_list[y] = longTermTrend['Ticker'][y]
    
        if request.form.get('test3'):
            # Activate Test 2
            print('Test 3 Activated')
            
            for y in number_array:
                display_list[y] = "Not Mike"
    
    
    return render_template('index.html', tick = display_list) #random.sample(tickers_list, 10))


@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        min = request.form['min']
        max = request.form['max']
        trend = request.form.get('trend')
        print("variables: " + min + max + trend,file=sys.stderr)
        
        if min != '' and max != '':
            chosen_stock = ''
            yearDF = pd.DataFrame()
            tickers_list = ['AAPL', 'EBAY', 'NUE', 'F', 'TME', 'TWTR', 'RBLX',
                                'PFE', 'T', 'WFC', 'MSFT', 'INTC', 'TSLA', 'PYPL', 'HOOD', 'DIS']
            for tick in tickers_list:
                onDayDF = yf.Ticker(tick).history(period='1d')
                if float(max) >= onDayDF['Close'][-1] >= float(min):
        
                    yearDF = yf.Ticker(tick).history(period = '1y')
                    if (trend == 'positive' and yearDF['Close'][0] < yearDF['Close'][-1]) or (trend == 'negative' and yearDF['Close'][0] > yearDF['Close'][-1]):
                        chosen_stock = tick
        

            yearDF = yf.Ticker(chosen_stock).history(period = '1y')
            #plots closing value over time for chosen stock
            plt.clf()
            plt.plot(yearDF.index, yearDF['Close'])
            plt.ylabel('Dollars')
            try:
                plt.title(yf.Ticker(chosen_stock).info['longName'] + "(" + chosen_stock +")")
            except:
                print("no value in chosen_stock")
            plt.savefig("FrontEnd\BAWS\static\images\plot1pic.png")
            return render_template('recommend_page.html', error = "")
        else:
            return render_template('recommend_page.html', error = "Please fill in minimum and maximum price")
        
        
        
        
        
        
    return render_template('recommend_page.html', error = "")

@app.route('/sign_up', methods=['GET', 'POST'])
def user_data():
    if request.method == 'POST':
        sign_up_file = pd.read_csv('FrontEnd/BAWS/FileStorage/user.csv')
        USERNAME = str(request.form['Username'])
        PASSWORD = str(request.form['Password'])
        REPASSWORD = str(request.form['RePassword'])
        if REPASSWORD == PASSWORD:
            input_data = pd.DataFrame()
            input_data['Username'] = [USERNAME]
            input_data['Password'] = [PASSWORD]
            sign_up_file = sign_up_file.append(input_data, ignore_index = True)
            print(sign_up_file, file=sys.stderr)
            sign_up_file.to_csv('FrontEnd/BAWS/FileStorage/user.csv', index=False)
            return redirect(url_for('views.home'))
    return render_template('sign_up.html')

@app.route('/addStock', methods=['GET', 'POST'])
def stock_search():
    watch_list = []
    tickers_list = ['aapl', 'ebay', 'nue', 'f', 'tme', 'twtr', 'rblx', 'pfe', 't', 'wfc', 'msft', 'intc', 'tsla', 'pypl', 'hood', 'dis']
    if request.method == 'POST':
        #ticker_list gives the list of stocks 
        #text is the stock that the user input
        text = str(request.form['Tickers'])
        watch_list.append(text)
        
        getStockInfo.generate_graph(text)
        
        #print to see what the user has typed
        print("The text is: ", text, file =sys.stderr)
        
        if text in tickers_list:
            #searches yahoo finance for tickers from the ticker_list 
            tickers = yf.Tickers(tickers_list)
             #downloads everything to do with tickers into the code so that we can use it
            df = tickers.download(group_by='ticker')
            #prints the info for the stock that the user typed in (SUPPOSED TO!!)
            print(df[text.upper()], file =sys.stderr)
        else:
            tickers = yf.Ticker(text).history(period = '1y')
        #prints the list of tickers from tickers
        print(tickers, file =sys.stderr)
        #adds whatever the user typed into the ticker_list
        tickers_list.append(text)
        #prints the list with the added ticker
        print(tickers_list, file =sys.stderr)
        #df.plot.line()
        return render_template("addStock.html", tick = watch_list, text = text)
    return render_template("addStock.html", tick = watch_list)

def create_app():
    
    app.config
    
    from .views import views
    
    app.register_blueprint(views, url_prefix='/')
    
    return app