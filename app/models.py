from app import db
from enum import unique
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

@login.user_loader
def load_user(id):
    return Student.query.get(int(id))

enrolled = db.Table('enrolled', 
                     db.Column('studentid', db.Integer, db.ForeignKey('student.id')),
                     db.Column('classid', db.Integer, db.ForeignKey('class.id'))
                     )

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coursenum = db.Column(db.String(3))  
    title = db.Column(db.String(150))
    major = db.Column(db.String(20), db.ForeignKey('major.name'))
    roster = db.relationship(
        'Student', secondary=enrolled,
        primaryjoin=(enrolled.c.classid == id), lazy='dynamic', overlaps="classes")
    def __repr__(self):
        return '<Class id: {} - coursenum: {}, title: {}, major: {}>'.format(self.id, self.coursenum, self.title, self.major)
    def getTitle(self):
        return self.title

class Major(db.Model):
    name = db.Column(db.String(20), primary_key=True)
    department = db.Column(db.String(150))
    classes = db.relationship('Class', backref='coursemajor', lazy='dynamic')
    def __repr__(self):
        return '<Major name: {} - department: {}>'.format(self.name, self.department)

class Student(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique=True, index = True) #usernames are unique
    password_hash = db.Column(db.String(128))
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    address = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, index=True)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow) # tracks time
    
    classes = db.relationship(
        'Class', secondary=enrolled,
        primaryjoin=(enrolled.c.studentid == id), lazy='dynamic', overlaps="roster")
    
    def __repr__(self):
        return '<student {} - {} {} - {};>'.format(self.id, self.firstname, self.lastname, self.email)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def enroll(self, newClass):
        # check if student is not enrolled in that class
        if not self.is_enrolled(newClass):
            self.classes.append(newClass)

    def unenroll(self, oldclass):
        if self.is_enrolled(oldclass):
            self.classes.remove(oldclass)

    def is_enrolled(self, newclass):
        # self refers to the student object.
        self.classes.filter(enrolled.c.classid == newclass.id).count() > 0 # if greater than zero then the student is enrolled in the class
        
    def enrolledCourses(self):
        return self.classes