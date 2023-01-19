from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME='database.db'
DB_PATH = path.join(path.dirname(__file__), DB_NAME)



def createToDoApp():
    
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "hkhlkhuiihljklytljlj"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    
    from .models import User, Note 
    
    create_database(app)
    
    
    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created database!')