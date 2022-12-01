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

class Add_Appointment(db.Model):
    _id = db.Column("id",db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    phonenumber = db.Column(db.Integer)
    email = db.Column(db.String(255))
    date = db.Column(db.String(255))
    time= db.Column(db.String(255))
    poa = db.Column(db.String(255))
    msg = db.Column(db.String(255))
    
    def __init__(self,firstname,lastname,phone_number,email,date,time,poa,msg):
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phone_number
        self.email = email
        self.date = date
        self.time = time
        self.poa = poa
        self.msg = msg

class Add_Order(db.Model):
    _id = db.Column("id",db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    phonenumber = db.Column(db.Integer)
    email = db.Column(db.String(255))
    product = db.Column(db.String(255))
    quantity = db.Column(db.String(255))
    msg = db.Column(db.String(255))
    
    def __init__(self,firstname,lastname,phone_number,email,product,quantity,msg):
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phone_number
        self.email = email
        self.product = product
        self.quantity = quantity
        self.msg = msg

with app.app_context():
    db.create_all()