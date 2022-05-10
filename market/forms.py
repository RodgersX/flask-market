from tokenize import String
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from market.models import User


class RegisterForm(FlaskForm):
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(
            email_address=email_address_to_check.data
        ).first()

        if email_address:
            raise ValidationError(
                "Email address already exists! Please try a different email."
            )

    username = StringField(
        label="User Name:",
        validators=[
            Length(
                min=2,
                max=30,
                message="The username should be between 2 and 30 characters",
            ),
            DataRequired(),
        ],
    )
    email_address = StringField(
        label="Email Address:",
        validators=[
            Email(),
            DataRequired(),
        ],
    )
    password = PasswordField(
        label="Password:",
        validators=[
            Length(min=6),
            DataRequired(),
        ],
    )
    pass_confirm = PasswordField(
        label="Confirm Password:",
        validators=[
            EqualTo("password"),
            DataRequired(),
        ],
    )
    submit = SubmitField(label="Create Account")


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password=PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label="Sign In")