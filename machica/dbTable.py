from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from settings import db, app

class UserInfo(db.Model):
    _id = db.Column("id",db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    phonenumber = db.Column(db.Integer)
    email= db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self,firstname,lastname,gender,phonenumber,email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.phonenumber = phonenumber
        self.email = email
        self.password = password

        

with app.app_context():
    db.create_all()