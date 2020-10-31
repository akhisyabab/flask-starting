import threading
from datetime import datetime
from threading import Thread

import ast
import backoff
import pandas as pd
import requests
from bs4 import BeautifulSoup
from flask import Blueprint, request, url_for, render_template, make_response, Response, redirect, flash
from flask import current_app
from flask_login import login_user, current_user, login_required, logout_user
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import text

from project import db
from project.models.models import User
from project.utils.date import date2str
from project.utils.exceptions import NotFound

app_blueprint = Blueprint('appblueprint', __name__, template_folder='templates', static_folder='static')


@app_blueprint.route('/')
@login_required
def home():
    print("LIST OF ENUMERATION: ")
    print(threading.enumerate())
    response = render_template('index.html')
    return response


@app_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        username = username.lower()
        current_user = User.find_by_username(username)
        if not current_user:
            flash('ERROR! user not found.', 'error')
            return redirect(url_for('appblueprint.login'))

        if User.verify_hash(password, current_user.password):
            current_user.authenticated = True
            db.session.add(current_user)
            db.session.commit()
            login_user(current_user)

            return redirect(url_for('appblueprint.home'))
        else:
            db.session.rollback()
            flash('ERROR! Incorrect login credentials.', 'error')

    return render_template('login.html')


@app_blueprint.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('appblueprint.login'))


@app_blueprint.route('/profile/<username>', methods=['GET', 'POST'])
@login_required
def profile(username):
    current_user = User.find_by_username(username)
    return render_template('profiles.html', user=current_user)


