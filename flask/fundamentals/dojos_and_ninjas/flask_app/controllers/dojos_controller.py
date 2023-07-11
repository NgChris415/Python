from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojos_model import Dojos


@app.route('/') #Get request for 127.0.0.1:5000
def dojo_home():
    return render_template('dojos.html', dojos = Dojos.get_dojos())

@app.route('/create', methods=['POST']) #Post request route
def add_dojo():
    Dojos.add_dojo(request.form)
    return redirect('/')

@app.route('/show_dojo/<int:dojo_id>')
def show_dojo(dojo_id):
    return render_template('show_dojo.html', ninjas = Dojos.get_all_ninjas(dojo_id), dojo=Dojos.get_dojo(dojo_id))