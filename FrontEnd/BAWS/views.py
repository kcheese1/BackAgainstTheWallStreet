from flask import Blueprint, render_template

views = Blueprint("views", __name__, template_folder = 'template')

#making a route that shows the login page
@views.route('/')
def home():
    #returns to login page 
    return render_template("loginPage.html")

#making a route that shows the sign up page
@views.route('/sign_up')
def sign_up():
    #returns to sign up page 
    return render_template("sign_up.html")

#making a route that shows the index page
@views.route('/index')
def index():
    #returns to index page 
    return render_template("index.html")

#making a route that shows the add stock page
@views.route('/addStock')
def addStock():
    #returns to add stock page 
    return render_template("addStock.html")

#making a route that shows the help desk page
@views.route('/helpDesk')
def helpDesk():
    #returns to help desk page 
    return render_template("helpDesk.html")

#making a route that shows the recommend stock page
@views.route('/recommend')
def recommend():
    #returns to recommend page 
    return render_template("recommend_page.html")