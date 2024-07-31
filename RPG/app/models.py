from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role_id = db.Column(db.Integer, nullable=False, default=1)

    def __repr__(self):
        return f"id-{self.id}_name-{self.username}"

    def __str__(self):
        return f"User: {self.username}"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
