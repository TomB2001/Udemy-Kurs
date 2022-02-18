from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'hello World!'

@app.route('/halloDu')
def hello_world_fancy():
    return """
    <html>
    <body>

    <h1>Hello World!</h1>
    <p>Hallo</p>

    </body>
    </html>
    """