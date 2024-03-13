from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import  ValidationError, Length, DataRequired
from app.models import Class, Major
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

