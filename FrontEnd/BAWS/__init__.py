from flask import Flask, render_template
from os import path
import sys


app = Flask(__name__)


@app.route('/login', methods = ["GET", "POST"])
def getLoginData():
    username = "dddd"
    password = "ssss"
    
    print(username, file=sys.stderr)
    
    
    return render_template("loginPage.html")


def create_app():
    
    
    
    from .views import views
    
    app.register_blueprint(views, url_prefix='/')
    
    return app