from flask import Flask

app = Flask(__name__)


@app.route('/',strict_slashes=False)
def hello():
    return '<h1>Hello HBNB!</h1>'
