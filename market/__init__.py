from enum import unique
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"

#important to display the form
app.config["SECRET_KEY"] = "64365cef65864818c201dfa2" 
db = SQLAlchemy(app)

from market import routes
