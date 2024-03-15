from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import  ValidationError, Length, DataRequired, Email, EqualTo
from app.models import Class, Major, Student
from wtforms_sqlalchemy.fields import QuerySelectField

# Forms handle submitted data by the user.
# when the user interacts with the web browser and
# submits information online, a form is also activated and submitted.

# Examples where forms are used: 
#   1. Ordering a product online, 
#   2. filtering custom views, 
#   3. gathering text, 
#   4. updating your information online, 
#   5. collecting feedback

# QUERY SELECT FIELD: allows us to get data from database and dynamically populate options in the dropdown list.
def get_major():
    return Major.query.all()

def get_majorlabel(theMajor):
    return theMajor.name

class ClassForm(FlaskForm):
    coursenum = StringField('Course Number',[Length(min=3, max=3)])
    title = StringField('Course Title', validators=[DataRequired()]) # textbox
    major = QuerySelectField('Majors', query_factory = get_major, get_label = get_majorlabel, allow_blank=False) # drop down feature to select major
    submit = SubmitField('Post')

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