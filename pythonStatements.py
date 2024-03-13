
from app import db
#create the database file, if it doesn't exist. 
db.create_all()

# import db models
from app.models import Class

# import major model 
from app.models import Major

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
from app.models import Class
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