from flask_login import LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sergeantsnape'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_NAME
    db.init_app(app)

    from .presentation import presentation
    from .auth import auth
    from .functions import functions

    app.register_blueprint(presentation, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(functions, url_prefix='/')

    from .model import User,Todo

    create_db(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        try:
            return User.query.get(int(user_id))
        except:
            return None

    return app

def create_db(app):
    if not path.exists('webpage/'+DB_NAME):
        db.create_all(app = app)
        print('DB CREATED')