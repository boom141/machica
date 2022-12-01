import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, redirect,url_for,render_template,session,request,flash
from datetime import datetime
from dbTable import *
from settings import app,db

@app.route('/', methods=['POST','GET'])
def landing():
    if 'user' in session:
        if request.form == 'POST':
            query_email = request.form['email']
            query_msg = request.form['message']
            return redirect(url_for('inquiry', email=query_email, message=query_msg))
        else:
            return render_template('landing.html', user_in_session = session['user'][0].upper())
    else:
        return render_template('landing.html', user_in_session = None)
   

@app.route('/login', methods=['POST','GET'])
def login():
    if 'user' in session:
        return redirect(url_for('landing'))
    else:
        if request.method == 'POST':
            user_email = request.form['email']
            user_password = request.form['password']
            
            email_exist = UserInfo.query.filter_by(email=user_email).first()
            password_exist = UserInfo.query.filter_by(password=user_password).first()

            if email_exist and password_exist:
                session.permanent = True
                session['user'] = email_exist.firstname
                return redirect(url_for('landing'))
            else:
                flash(' Your account is not registered yet.')
                return redirect(url_for('login', user_in_session = None))

        else:
            return render_template('login.html',user_in_session = None)

@app.route('/register', methods=['POST','GET'])
def register():
    if 'user' in session:
        return redirect(url_for('landing'))
    else:
        if request.method == 'POST':
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
                return redirect(url_for('register', user_in_session = None))
            elif password != confirm_password:
                flash(' Password repeatition is not validated.')
                return redirect(url_for('register', user_in_session = None))
            else:
                Add_User = UserInfo(firstname,lastname,gender,int(phone_number),user_email, password)
                db.session.add(Add_User)
                db.session.commit()
                return redirect(url_for('landing'))

        else:
            return render_template('register.html', user_in_session = None)


@app.route('/appointment', methods=['POST','GET'])
def appointment():  
    if 'user' in session:
        if request.method == 'POST':
            firstname = request.form['first-name']
            lastname = request.form['last-name']
            phone_number = request.form['phone-number']
            email = request.form['email']
            date = request.form['date']
            time = request.form['time']
            poa = request.form['POA']
            msg = request.form['message']

            if(not firstname and not lastname and not phone_number and not date and not time):
                flash(' You should check in on some of those fields above.')
                return render_template('appointment.html',  user_in_session = session['user'][0].upper())
            else:
                appointment = Add_Appointment(firstname,lastname,int(phone_number),email,str(date),str(time),poa,msg if msg else 'none')
                db.session.add(appointment)
                db.session.commit()
                flash('Your booking has been confirmed. Check your email for details.')
                return render_template('appointment.html',  user_in_session = session['user'][0].upper())
        else:
            return render_template('appointment.html',  user_in_session = session['user'][0].upper())
    else:
        return redirect(url_for('login', user_in_session = None))

@app.route('/order', methods=['POST','GET'])
def order():
    if 'user' in session:
        if request.method == 'POST':
            firstname = request.form['first-name']
            lastname = request.form['last-name']
            phone_number = request.form['phone-number']
            email = request.form['email']
            product = request.form['pr-name']
            quantity = request.form['quantity']
            msg = request.form['message']

            if(not firstname and not lastname and not phone_number and not product and not quantity):
                flash(' You should check in on some of those fields above.')
                return render_template('order.html',  user_in_session = session['user'][0].upper())
            else:
                order = Add_Order(firstname,lastname,phone_number,email,product,quantity,msg if msg else 'none')
                db.session.add(order)
                db.session.commit()
                flash('Your order has been confirmed. Check your email for details.')
                return render_template('order.html',  user_in_session = session['user'][0].upper())
        else:
            return render_template('order.html',  user_in_session = session['user'][0].upper())
    else:
        return redirect(url_for('login', user_in_session = None))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('landing'))


@app.route('/inquiry/<email>/<message>')
def inquiry(email,message):

    mail_content = f'User {email} ask,{message}' 
    #The mail addresses and password
    sender_address = 'otpsender47@gmail.com'
    sender_pass = 'xisnpznnkhkhcbls'
    receiver_address = 'josephnava911@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'ONE TIME PIN REGISTRATION.'   #The subject line
    
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
   
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

if __name__ == '__main__':
    app.run(debug=True)