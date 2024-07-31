from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Email, Length, ValidationError


class LoginForm(FlaskForm):
    email = StringField(
        "Email", [Email(message="Wrong address format."), DataRequired()]
    )
    password = PasswordField(
        "Password",
        [DataRequired()],
    )
    submit = SubmitField("Submit")