from config import Config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
admin = Admin()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)

    Migrate(app, db)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    with app.app_context():
        db.create_all()

    return app
