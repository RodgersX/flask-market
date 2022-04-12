from ast import Pass
import email
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label="User Name:")
    email_address = StringField(label="Email Address:")
    password = PasswordField(label="Password:")
    pass_confirm = PasswordField(label="Confirm Password:")
    submit = SubmitField(label="Create Account")
