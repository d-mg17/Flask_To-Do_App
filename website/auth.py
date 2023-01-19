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

        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password")
        password2 = request.form.get("password-confirmation")

        if len(email) < 7:
            flash("Email too short. Enter a valid email.", "error")
        elif len(username) < 2:
            flash(
                "Username too short, must be at least 2 characters.", "error"
            )
        elif len(password1) < 7:
            flash(
                "Password too short, must be at least 8 characters.", "error"
            )
        elif password1 != password2:
            flash("Passwords don't match.", "error")
        else:
            flash("Creating account...", "success")
            # Add user to database
            flash('Account created!', 'success')
    return render_template("signup.html")
