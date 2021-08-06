from .model import User
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Welcome back!',category='success')
                login_user(user, remember=True)
                return redirect(url_for('presentation.home'))
            else:
                flash('Invalid password. Try again',category='error')
        else:
            flash('User not found',category='error')
    return render_template('login.html',user=current_user)

@auth.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('presentation.welcome'))

@auth.route('signup',methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password1 = request.form['password1']
        password2 = request.form['password2']
        name = request.form['name']

        if password1 != password2:
            flash('Password not match', category='error')
        else:
            if db.session.query(User).filter_by(email=email).count()<1:
                new_user = User(email=email, password=generate_password_hash(password1), name=name)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('Signed up successfully', category='success')
                
                return redirect(url_for('presentation.home'))
            else:
                flash('User already exists', category='error')

    return render_template('signup.html',user=current_user)