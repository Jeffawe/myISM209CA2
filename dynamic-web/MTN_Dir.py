from flask import Flask, render_template, request, session

import models

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bookexampledbpassword@localhost/bookexample'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = b'\x06Y\xe6!Z\x85W\xe2/\x15FG\xe0\x17Xk\xa1\x92\xcdIn\xa5\r\x13'

db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template('home.html', title="Home")


@app.route("/signup/")
def signup():
    return render_template('signup.html', title="Register", information="Use the form displayed to register")


@app.route("/process-signup/", methods=['POST'])
def process_signup():
    # Let's get the request object and extract the parameters sent into local variables.
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    residential_address= request.form['residential_address']
    DOB = request.form['DOB']
    NIN = request.form['NIN']
    nationality = request.form['nationality']

    try:
        user = models.User(firstname=firstname, lastname=lastname, residential_address=residential_address, DOB=DOB, NIN=NIN, nationality=nationality)
        db.session.add(user)
        db.session.commit()

    except Exception as e:
        # Error caught, prepare error information for return
        information = 'Could not submit. The error message is {}'.format(e.__cause__)

        return render_template('signup.html', title="SIGN-UP", information=information)

    # If we have gotten to this point, it means that database write has been successful. Let us compose success info

    # Let us prepare success feedback information

    information = 'User by name {} {} successfully added. The login name is the email address {}.'.format(firstname, lastname,)

    return render_template('signup.html', title="SIGN-UP", information=information)



@app.errorhandler(404)
def page_not_found(error):
    return render_template('page-not-found.html'), 404


if __name__ == "__main__":
    app.run(port=5001)