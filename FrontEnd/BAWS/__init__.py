from flask import Flask, render_template, request, Blueprint, redirect, url_for
import pandas as pd
from os import path
import yfinance as yf
import sys

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
    return render_template('index.html')

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
    if request.method == 'POST':
        #ticker_list gives the list of stocks 
        tickers_list = ['aapl', 'ebay', 'nue', 'f', 'tme', 'twtr', 'rblx', 'pfe', 't', 'wfc', 'msft', 'intc', 'tsla', 'pypl', 'hood', 'dis']
        #text is the stock that the user input
        text = str(request.form['Tickers'])
        
        #print to see what the user has typed
        print("The text is: ", text, file =sys.stderr)
        
        #searches yahoo finance for tickers from the ticker_list
        tickers = yf.Tickers(tickers_list)
        #prints the list of tickers from tickers
        print(tickers, file =sys.stderr)
        #adds whatever the user typed into the ticker_list
        tickers_list.append(text)
        #prints the list with the added ticker
        print(tickers_list, file =sys.stderr)
        
        #downloads everything to do with tickers into the code so that we can use it
        df = tickers.download(group_by='ticker')
        #prints the info for the stock that the user typed in (SUPPOSED TO!!)
        print(df[text.upper()], file =sys.stderr)
        #df.plot.line()
        return render_template("addStock.html")
    return render_template("addStock.html")

def create_app():
    
    app.config
    
    from .views import views
    
    app.register_blueprint(views, url_prefix='/')
    
    return app