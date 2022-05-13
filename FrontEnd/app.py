from BAWS import create_app

#Standard setup for Flask application
app = create_app()
if __name__ == '__main__':
    app.run(debug=True)