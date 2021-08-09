from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3 as sql

app = Flask(__name__, template_folder='templates')

app.config['SQLANCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SECRET_KEY'] = 'random string'

db = SQLAlchemy(app)


class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    location = db.Column(db.String(200))
    email = db.Column(db.String(100))


def __init__(self, name, city, location, email):
    self.name = name
    self.city = city
    self.location = location
    self.email = email


@app.route('/enternew')
def new_student():
    return render_template('student.html')


@app.route('/show_all')
def show_all():
    return render_template('show_all.html', students=students.query.all())


@app.route('/city', methods=['GET', 'POST'])
def city():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            city1 = request.form['city']
            loc = request.form['location']
            email_id = request.form['email']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name, city, location, email) VALUES(?,?,?,?)",
                            (nm, city1, loc, email_id))

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in data insertion "
        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] \
                or not request.form['location'] or not request.form['email']:
            flash("Please Enter all the Fields", 'error')
        else:
            student = students(request.form['name'], request.form['city'],
                               request.form['lcoation'], request.form['email'])

            db.session.add(student)
            db.session.commit()

            flash('Record added Successfully')
            return redirect(url_for('show_all'))
    return render_template('new.html')


if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()
