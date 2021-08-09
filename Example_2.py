from flask import Flask, redirect,url_for

app = Flask(__name__)


@app.route('/admin')
def helloAdmin():
    return 'Hello Shyam You are genius'


@app.route('/guest/<guest>')
def helloGuest(guest):
    return 'Hello %s as Guest' %guest


@app.route('/user/<name>')
def helloUser(name):
    if name == 'admin':
        return redirect(url_for('helloAdmin'))
    else:
        return redirect(url_for('helloGuest',guest=name))


if __name__=="__main__":
    app.run(debug=True)