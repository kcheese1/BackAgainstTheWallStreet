from flask import Blueprints, render_template

views = Blueprints("views", __name__)

@views.route('/')
def home():
    return render_template("index.html")