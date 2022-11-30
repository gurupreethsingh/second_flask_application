from flask import Flask
app =  Flask(__name__)


def index():
    return """
            <html>
             <body>
               <h1>Hello second flask app</h1>
               <h2>This is the second line.</h2>
             </body>
            </html>
            """


if __name__ == "__main__":
    app.run(debug =True)