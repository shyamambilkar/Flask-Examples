from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<html><body><h1> Hello Jayashri working hard on your study</h1></body></html>'


if __name__ == "__main__":
    app.run(port=8080, debug=True)
