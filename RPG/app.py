from app import create_app, db, admin
from app.models import User
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role_id == 3


app = create_app()
admin.add_view(AdminModelView(User, db.session))


@app.shell_context_processor
def make_shell_context():
    """Add database object and models to Flask shell context."""
    return dict(
        db=db,
        User=User
    )


if __name__ == "__main__":
    app.run()
