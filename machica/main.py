from flask import Flask, redirect,url_for,render_template,session,request
from datetime import datetime
# from dbTable import *
from settings import app,db

@app.route('/')
def landing():
   return render_template('landing.html')




if __name__ == '__main__':
    app.run(debug=True)