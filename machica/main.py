from flask import Flask, redirect,url_for,render_template,session,request,flash
from datetime import datetime
from dbTable import *
from settings import app,db

@app.route('/')
def landing():
   return render_template('landing.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods=['POST','GET'])
def register():
    if 'user' in session:
        return redirect(url_for('landing'))
    else:
        if request.method == 'POST':
            genders = ['male-option', 'female-option', 'other-option']

            firstname = request.form['first-name']
            lastname = request.form['last-name']
            gender = request.form['gender']
            phone_number = request.form['phone-number']
            user_email = request.form['email']
            password = request.form['password']
            confirm_password = request.form['confirm-password']

            email_exist = UserInfo.query.filter_by(email=user_email).first()

            if email_exist:
                flash(' Email is already taken, please use another email.')
                return redirect(url_for('register'))
            elif password != confirm_password:
                flash(' Password repeatition is not validated.')
                return redirect(url_for('register'))
            else:
                Add_User = UserInfo(firstname,lastname,gender,int(phone_number),user_email, password)
                db.session.add(Add_User)
                db.session.commit()
                return redirect(url_for('landing'))

        else:
            return render_template('register.html')





        

@app.route('/appoinment')
def appointment():
    return render_template('appointment.html')

@app.route('/order')
def order():
    return render_template('order.html')


if __name__ == '__main__':
    app.run(debug=True)