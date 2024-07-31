from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from .. import db
from . import main
from .forms import LoginForm


@main.route('/')
def home():
    return render_template("index.html")
