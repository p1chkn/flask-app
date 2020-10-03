from flask import Flask


app = Flask(__name__)


@app.rout('/')
def hello_world():
    return "I'm done it!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')