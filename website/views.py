from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint("views",__name__)

@views.route('/')
def index():
    return render_template("index.html", user=current_user)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("new_note")
        
        if len(note) < 2:
            flash(message="Note is too short!", category="error")
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash(message="Note added!", category="success")

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    note = json.loads(request.data)
    note_id = note['noteId']
    target_note = Note.query.get(note_id)
    if target_note:
        if target_note.user_id == current_user.id:
            db.session.delete(target_note)
            db.session.commit()
            return jsonify({"message": "Note deleted!"})
    return jsonify({"message": "Note not found."})