from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninjas_model import Ninjas
from flask_app.models.dojos_model import Dojos 


@app.route('/ninjas') #Get request for 127.0.0.1:5000
def ninja_page():
    return render_template('ninjas.html', ninjas = Ninjas.get_ninjas(), dojos = Dojos.get_dojos())

@app.route('/ninjas/create', methods=['POST']) #Post request route
def create_ninja():
    Ninjas.add_ninja(request.form)
    return redirect('/')

