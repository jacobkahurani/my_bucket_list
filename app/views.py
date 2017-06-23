# views.py

from flask import render_template
from flask import request
from app import app

@app.route('/')
def index():
    #query = request.args.get("user name", password)
    return render_template("index.html")

@app.route('/login',methods=['POST','GET'])
def login():
    if valid_login(request.form['username'],request.form['password']):
        return log_the_user_in(request_form['username'])
    else:
        error ='Invalid name or password'
    return render_template(index.html, error=error)
    
@app.route('/signup')
def signup():
    return render_template("ui_signup.html")

@app.route('/bucketlist')
def bucketlistUI():
    return render_template("ui.html")

@app.route('/bucketlist_activity')
def bucketlistActivity():
    return render_template("bucket_list_activity_ui.html")