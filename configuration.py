from flask import Flask, render_template, request, url_for, redirect, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__name__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'dart.sqlite')
app.secret_key = "123"
app.permanent_session_lifetime = timedelta(minutes=5)
db = SQLAlchemy(app)
Migrate(app, db)

class evenement(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    cafe = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    time = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    beloweighteen = db.Column(db.BOOLEAN)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Add(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enaam = db.Column(db.String(1000))
    email = db.Column(db.String(1000))


from routes import routing

db.create_all();

