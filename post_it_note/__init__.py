from flask import Flask
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager
from flask_pagedown import PageDown
from flask_sqlalchemy import SQLAlchemy
from post_it_note.config import DevConfig

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
pagedown = PageDown()

def create_app(config=DevConfig()):
    app = Flask(__name__)
    app.config.from_object(config)
    config.init_app(app)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)

    return app