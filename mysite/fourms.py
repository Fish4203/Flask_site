from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from models import User

class Login(FlaskForm):
    Username = StringField('username', validators=[DataRequired()])
    Password = PasswordField('password', validators=[DataRequired()])
    Save = BooleanField('rember me')
    Sign_in = SubmitField('Sign in')

class Sign_up(FlaskForm):
    Username = StringField('username', validators=[DataRequired()])
    Emailenter = StringField('email', validators=[DataRequired(), Email()])
    Password = PasswordField('password', validators=[DataRequired()])
    Passwordcheck = PasswordField('passwordcheck', validators=[DataRequired(), EqualTo('Password')])
    submit = SubmitField('sign up')

    def validate_email(self, Emailenter):
        used = User.query.filter_by(Email=Emailenter).first()
        if used is not None:
            raise ValidationError('Please use a different Email')

    def validate_username(self, Username):
        used = User.query.filter_by(Name=Username).first()
        if used is not None:
            raise ValidationError('Please use a different username')

class Postmain(FlaskForm):
    Post_title = TextField('post_title', validators=[DataRequired()])
    Post_body = TextField('post_body', validators=[DataRequired()])
    submit = SubmitField('Post')

class Profile_form(FlaskForm):
    pass
