from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField,  BooleanField, SubmitField)


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')