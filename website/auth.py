from flask import Blueprint, render_template, redirect, request, flash

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    # data = request.form
    # print(data)
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return redirect("/")


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":

        email = request.form.get(key="email")
        username = request.form.get(key="username")
        password1 = request.form.get(key="password")
        password2 = request.form.get(key="password-confirmation")

        if len(email) < 7:
            flash("Email too short. Enter a valid email.", category="error")
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
            # Add user to database
            pass
    return render_template("signup.html")
