
from app import db

# import db models
from app.models import Class, Major, Student, Enrolled
from datetime import datetime

#create the database file, if it changes. 
db.create_all()
c1 = Class.query.filter_by(coursenum = '321').filter_by(major='CptS').first()
c2 = Class.query.filter_by(coursenum = '322').filter_by(major='CptS').first()
c3 = Class.query.filter_by(coursenum = '355').filter_by(major='CptS').first()
c4 = Class.query.filter_by(coursenum = '451').filter_by(major='CptS').first()

db.classes.add(c1)
db.classes.add(c2)
db.classes.add(c3)
db.session.commit()

s1 = Student(username = 'Jack', firstname = 'Jack', lastname = 'Adams', email='jadams@gmail.com')
s2 = Student(username = 'Daniel', firstname = 'Daniel', lastname = 'Kreeg', email='dk@gmail.com')
db.session.add(s1)
db.session.add(s2)
db.session.commit()

s1 = Student.query.filter_by(username='Jack').first()
s2 = Student.query.filter_by(username='Daniel').first()

c1 = Class.query.filter_by(coursenum='322').first()
c2 = Class.query.filter_by(coursenum='355').first()
c3 = Class.query.filter_by(coursenum='451').first()

# Alternative ways to enroll students
assoc1 = Enrolled(enrolldate=datetime.utcnow())
assoc1.classenrolled = c1
assoc1.studentenrolled = s1
db.session.add(assoc1)
db.session.commit()

assoc2 = Enrolled(enrolldate=datetime.utcnow())
assoc2.classenrolled = c2
s1.classes.append(assoc2)
db.session.commit()

assoc3 = Enrolled(classenrolled = c3, enrolldate=datetime.utcnow())
s1.roster.append(assoc3)
db.session.commit()

assoc4 = Enrolled(studentenrolled = s2, enrolldate=datetime.utcnow())
s1.roster.append(assoc4)
db.session.commit()

assoc5 = Enrolled(studentenrolled = s2)
c2.roster.append(assoc5)
db.session.commit()

assoc6 = Enrolled(studentenrolled = s2, classenrolled = c3)
c2.roster.append(assoc6)
db.session.commit()

for c in c1.roster:
    print(c)

for s in s1.classes:
    print(s)

# create a major
newMajor = Major(name='CptS',department='School of EECS')
db.session.add(newMajor)
newMajor = Major(name='CE', department='Civil Engineering')
db.session.add(newMajor)
db.session.commit()
Major.query.all()
for m in Major.query.all():
    print(m)

# create a class; assign class majors to the major created above
newClass = Class(coursenum='322', major='CptS', title='Software Engineering')
db.session.add(newClass)
newClass = Class(coursenum='315', major ='CE', title='Fluid Mechanics')
db.session.add(newClass)
db.session.commit()

allClasses = Class.query.all()
Class.query.filter_by(major='CptS').all()
Class.query.filter_by(major='CptS').first()
Class.query.filter_by(major='CptS').order_by(Class.title).all()
Class.query.filter_by(major='CptS').count()

mymajor = Major.query.filter_by(name='CptS').first()

for c in mymajor.classes:
    print(c.title)

# create class objects and write them to the database
newClass = Class(coursenum='322')
db.session.add(newClass)
newClass = Class(coursenum='355')
db.session.add(newClass)
db.session.commit()

# query and print classes
Class.query.all()
Class.query.filter_by(coursenum='322').all()
Class.query.filter_by(coursenum='322').first()
myclasses = Class.query.order_by(Class.coursenum.desc()).all()

for c in myclasses:
    print(c.coursenum)

# A QUERY is a request for data or information from a database. 
# In the context of databases and information technology, a query is used to 
# retrieve data that matches specific criteria from a database, allowing users 
# to find the information they need.