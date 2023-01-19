from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import pymongo
import smtplib
import ssl
from email.message import EmailMessage

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://ad_work:jaykadel@cluster0.ocwlhjq.mongodb.net/?retryWrites=true&w=majority")
db = client.Ad_works

# client = MongoClient('mongodb+srv://jay_1020:jaykadel@cluster0.ocwlhjq.mongodb.net/?retryWrites=true&w=majority')
db = client["AD_Works"]
collection = db["User"]

email_sender = 'noreplyadworks@gmail.com'
email_password = 'dchfudiwhnoprekp'
email_receiver = ''

loggedin=False

class Database():
    def insert(self, username, email, password):
        filter={'email':email}
        result = client['AD_Works']['User'].find(
            filter=filter
        )
        if result!=1:
            user = {'username':username, 'email':email, 'password':password}
            collection.insert_one(user)
            return 1
        else :
            return 0
    
    def search(self, email, password):
        filter={'email':email}
        result = client['AD_Works']['User'].find(
            filter=filter
        )
        if result !=1:
            fiter={'password':password}
            result = client['AD_Works']['User'].find(
            filter=filter
            )
            if result != None:
                global loggedin
                loggedin=True
                return 1
        else :
            return 0 

dbo=Database()

@app.route('/')
def landing_page():
        return render_template('index.html',login=loggedin)

@app.route('/contact_us')
def contact_us():
    if loggedin==False:
        return render_template('index.html',warning='.',login=loggedin)
    else :
        return render_template('contact.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html',login=loggedin)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/services')
def services():
    print(loggedin)
    return render_template('services.html',login=loggedin)

@app.route('/contacting',methods=['post'])
def contacting():
    name=request.form['name']
    mobile=request.form.get('mobile')
    email=request.form.get('email')
    message=request.form.get('messages')
    subject = 'You have a request'
    body =f"""
Name: {name}
Mobile No.: {mobile}
Email: {email}
Description:
{message}
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    return render_template('contact.html',success='.')

@app.route('/perform_login',methods=['post','get'])
def perform_login():
    email=request.form.get('email')
    password=request.form.get('password')
    confirmpassword=request.form.get('confirmpassword')
    print(password)
    if confirmpassword == password:
        response=dbo.search(email, password)
        if response == 0:
            return render_template('login.html',fail1='.')
        if response == 1:
            return render_template('index.html',success1='.',login=loggedin)
    else:
        return render_template('login.html',wrongpass='.')

@app.route('/perform_register',methods=['post','get'])
def perform_register():
    username=request.form.get('username')
    email=request.form.get('email')
    password=request.form.get('password')
    confirmpassword=request.form.get('confirmpassword')
    if confirmpassword == password:
        response=dbo.insert(username, email, password)
        if response == 0:
            return render_template('login.html',fail='.')
        if response == 1:
            return render_template('login.html',success='.')
    else:
        return render_template('register.html',wrongpass='.')

@app.route('/logout')
def logout():
    global loggedin
    loggedin=False
    return render_template('index.html',login=loggedin)

if __name__ == '__main__':
    app.run(debug=True)