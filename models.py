from MTN_Dir import db
from datetime import date


class User(db.Model):
    __tablename__ = 'userregister'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), unique=False, nullable=False)
    lastname = db.Column(db.String(20), unique=False, nullable=False)
    residential_address = db.Column(db.String(100), unique=False, nullable=True)
    DOB= db.Column(db.Date, nullable=False, default=date.today())
    NIN = db.Column(db.Integer(50), primary_key=True)
    nationality = db.Column(db.String(100), unique=False, nullable=False)


def __repr__(self):
    return '<Register {}>'.format(self.id)

