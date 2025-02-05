from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import  ValidationError, Length, DataRequired, Email, EqualTo
from app.Model.models import Student




class RegistrationForm(FlaskForm):
    username =  StringField('Username', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = TextAreaField('Address', [Length(min=0, max=200)]) # TextAreaField makes an adjustedable textbox
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')]) # make sure passwords are the same
    submit = SubmitField('Register')

    def validate_username(self, username):
        student = Student.query.filter_by(username=username.data).first()
        if student is not None:
            raise ValidationError('The username already exists! Please use a different username.')
        
    def validate_email(self, email):
        student = Student.query.filter_by(email=email.data).first()
        if student is not None:
            raise ValidationError('The email already exists! Please use a different email address.')
        
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')