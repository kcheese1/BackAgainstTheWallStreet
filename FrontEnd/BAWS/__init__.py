from flask import Flask, render_template, request, Blueprint, redirect, url_for
import pandas as pd
from os import path
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

def create_app():
    
    app.config
    
    from .views import views
    
    app.register_blueprint(views, url_prefix='/')
    
    return app