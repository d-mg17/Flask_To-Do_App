from flask import Blueprint

auth = Blueprint("auth",__name__)

@auth.route('/login')
def login():
    return "<h3>Log in</h3>"

@auth.route('/logout')
def logout():
    return "<h3>Logging Out</h3>"

@auth.route('/signup')
def signup():
    return "<h3>Sign-Up</h3>"