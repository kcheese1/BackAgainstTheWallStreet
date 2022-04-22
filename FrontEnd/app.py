from BAWS import create_app

app = create_app()
print("Generic")
if __name__ == '__main__':
    app.run(debug=True)