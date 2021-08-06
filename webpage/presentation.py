from flask import Blueprint, render_template
from flask_login import login_required, current_user

presentation = Blueprint('presentation',__name__)

@presentation.route('/home')
@login_required
def home():
    return render_template('home.html',user=current_user)

@presentation.route('/')
def welcome():
    return render_template('welcome.html',user=current_user)