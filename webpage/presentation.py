from flask import Blueprint, render_template
from flask_login import login_required, current_user

presentation = Blueprint('presentation',__name__)

@presentation.route('/home')
@login_required
def home():
    name = current_user.name
    return render_template('home.html',user=current_user,name=name)

@presentation.route('/')
def welcome():
    return render_template('welcome.html',user=current_user)

@presentation.route('/profile')
@login_required
def profile():
    name=current_user.name
    return render_template('profile.html',user=current_user,name=name)