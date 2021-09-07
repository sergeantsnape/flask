from .model import User
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, logout_user, login_required, current_user

functions = Blueprint('functions',__name__)

@functions.route('/deleteUser')
@login_required
def delete_user():
    email = User.query.filter_by(email=current_user.email).first()
    db.session.delete(email)
    db.session.commit()
    return redirect(url_for('presentation.welcome'))

@functions.route('/deleteNote')
@login_required
def delete_note():
    pass

@functions.route('/updateNote')
@login_required
def update_note():
    pass

@functions.route('/updateUser')
@login_required
def update_user():
    pass

@functions.route('/updatePassword',methods=['POST','GET'])
@login_required
def update_password():
    if request.method == 'POST':
        oldPassword = request.form['emailpassword']
        newPassword = request.form['newPassword1']
        confirmPassword = request.form['newPassword2']
        if check_password_hash(current_user.password,oldPassword):
            if newPassword == confirmPassword:
                current_user.password = generate_password_hash(newPassword)
                db.session.commit()
                flash('Your password has been updated!',category='success')
            else:
                flash('Password does not match',category='error')
        else:
            flash('Incorrect Password',category='error')

    return render_template('changePassword.html',user=current_user)