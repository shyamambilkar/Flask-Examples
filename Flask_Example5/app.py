from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3 as sql

app = Flask(__name__, template_folder='templates')


@app.route('/enternew')
def new_student():
    return render_template('student.html')


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


if __name__ == "__main__":
    app.run(debug=True)
