from BAWS import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# @app.route("/hello")
# def index():
#     return render_template("index.html")