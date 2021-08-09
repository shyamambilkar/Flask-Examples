from flask import Flask

app = Flask(__name__)


@app.route('/')
def Hello():
    return 'Hello Flask World..!'


@app.route('/myFlask')
def myFlask():
    return " Hello Patil and Jayashri Welcome to World of Flask"


if __name__ == "__main__":
    app.run(debug=True,port=8080)