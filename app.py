from flask import Flask
app =  Flask(__name__)


def index():
    return "<h1>Hello second flask app</h1>"


if __name__ == "__main__":
    app.run(debug =True)