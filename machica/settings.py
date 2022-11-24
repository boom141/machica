from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "YctkDFvaTj"
app.permanent_session_lifetime = timedelta(minutes=2)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)