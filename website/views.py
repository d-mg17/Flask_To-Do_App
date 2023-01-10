from flask import (Blueprint, redirect, render_template)

views = Blueprint("views",__name__)

@views.route('/')
def index():
    return render_template("index.html")
