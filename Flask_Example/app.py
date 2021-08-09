from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/login/<name>')
def success(name):
    return 'success %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == "__main__":
    app.run(debug=True, port=5002)
