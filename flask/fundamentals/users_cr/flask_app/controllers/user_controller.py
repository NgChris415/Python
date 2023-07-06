from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user_model import User 


@app.route('/') 
def home():
    return redirect('/user')

@app.route('/user') 
def user():
    return render_template('read_all.html', users = User.retrieve_all())

@app.route('/user/new_user')
def new_user():
    return render_template('create.html')

@app.route('/user/create_user' , methods=['POST'])
def create_user():
    print(request.form)
    User.save_user(request.form)
    return redirect('/user')