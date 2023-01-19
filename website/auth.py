from flask import Blueprint, render_template, redirect, request, flash, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.data.get('password')
        username = request.data.get('username')
    
        user = User.query.filter_by(username).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Welcome back!", category='success')
                redirect(url_for('views.index'))
            else:
                flash("Incorrect passsword, please try again", category='error')
        else:
            flash('User not found', category='error')

    
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return redirect(url_for('views.index'))


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":

        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password")
        password2 = request.form.get("password-confirmation")

        user = User.query.filter_by(username).first()
        if user:
            flash('Username already exists, please try again', category='error')
        elif len(email) < 7:
            flash("Email too short. Enter a valid email.", category= "error")
        elif len(username) < 2:
            flash(
                "Username too short, must be at least 2 characters.", category="error"
            )
        elif len(password1) < 7:
            flash(
                "Password too short, must be at least 8 characters.", category="error"
            )
        elif password1 != password2:
            flash("Passwords don't match.", category="error")
        else:
            flash("Creating account...", category="success")
            
            #Adding to database:
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()            
            
            flash('Account created!', 'success')
            
            return redirect(url_for('views.index'))
            
    return render_template("signup.html")
