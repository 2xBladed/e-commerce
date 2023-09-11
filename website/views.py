from flask import Blueprint, render_template


views = Blueprint('views', __name__)

@views.route('/')
def welcome():
    return render_template('welcome.html')

@views.route('/home')
def home():
    return "<h1> home page </h1>"