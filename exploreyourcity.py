from app import app # instructs to import every app from the application folder

if __name__ == '__main__':
    app.run(debug=True, port=8800)

# main file that flask/python will execute with debug on and port specified
# knows that there are other files that need to be executed
