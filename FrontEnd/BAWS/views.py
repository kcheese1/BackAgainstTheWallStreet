from flask import Blueprint, render_template

views = Blueprint("views", __name__, template_folder = 'template')

@views.route('/')
def home():
    return render_template("loginPage.html")

@views.route('/sign_up')
def sign_up():
    return render_template("sign_up.html")

@views.route('/index')
def index():
    return render_template("index.html")

@views.route('/addStock')
def addStock():
    return render_template("addStock.html")

@views.route('/recommend')
def recommend():
    return render_template("recommend_page.html")