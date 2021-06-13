from flask import Flask

app = Flask(__name__)


@app.route('/')
def counter():
    return 'customer login 0'
