from flask import Blueprint, render_template, flash, redirect, url_for, request
from app import db

from app.Controller.forms import ClassForm, EditForm, EmptyForm
from app.Model.models import Class
from flask_login import  current_user, login_required 
from config import Config

routes_blueprint = Blueprint('routes', __name__)
routes_blueprint.template_folder = Config.TEMPLATE_FOLDER #specify what is the template form for the routes so the templates can access them.

@routes_blueprint.route('/', methods=['GET'])
@routes_blueprint.route('/index', methods=['GET'])
@login_required
def index():
    eform = EmptyForm()
    allclasses = Class.query.order_by(Class.major).all()
    return render_template('index.html', title="Course List", classes = allclasses, eform = eform)

@routes_blueprint.route('/createclass/', methods=['GET', 'POST'])
@login_required
def createclass():
    cform = ClassForm()
    # handle rendering of the form
    if cform.validate_on_submit():
        newClass = Class(coursenum = cform.coursenum.data, title = cform.title.data, major = cform.major.data.name)
        db.session.add(newClass)
        db.session.commit()
        flash('Class "' + newClass.major + ' - ' + newClass.coursenum +'" is created')
        return redirect(url_for('index'))
    return render_template('create_class.html', form = cform)


@routes_blueprint.route('/display_profile', methods=['GET'])
@login_required
def display_profile():
    emptyform = EmptyForm()
    return render_template('display_profile.html', title='Display Profile', student = current_user, eform = emptyform)

@routes_blueprint.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    eform = EditForm()
    if request.method == 'POST':
        # handle form submission
        if eform.validate_on_submit():
            current_user.firstname = eform.firstname.data
            current_user.lastname = eform.lastname.data
            current_user.address = eform.address.data
            current_user.email = eform.email.data
            current_user.set_password(eform.password.data)
            db.session.add(current_user)
            db.session.commit()
            flash("Your changes have been saved")
            return redirect(url_for('routes.display_profile'))
        pass
    elif request.method == 'GET':
        # populate the user data from database
        eform.firstname.data = current_user.firstname
        eform.lastname.data = current_user.lastname
        eform.address.data = current_user.address
        eform.email.data = current_user.email
    else:
        pass
    return render_template('edit_profile.html', title='Edit Profile', form = eform)

@routes_blueprint.route('/roster/<classid>', methods=['GET'])
@login_required
def roster(classid):
    theClass = Class.query.filter_by(id = classid).first()
    return render_template('roster.html', title='Class Roster', current_class = theClass)

@routes_blueprint.route('/enroll/<classid>', methods=['POST'])
@login_required
def enroll(classid):
    eform = EmptyForm()
    if eform.validate_on_submit():
        theclass = Class.query.filter_by(id=classid).first()
        if theclass is None:
            flash('Class with id "{}" not found.'.format(classid))
            return redirect(url_for('index'))
        current_user.enroll(theclass)
        db.session.commit() # everytime you change the database, you make a commit
        flash('You are now enrolled in class {} {}!'.format(theclass.major, theclass.coursenum))
        return redirect(url_for('routes.index')) #reload, do a redirect to the index route
    else:
        return redirect(url_for('routes.index'))


@routes_blueprint.route('/unenroll/<classid>', methods=['POST'])
@login_required
def unenroll(classid):
    eform = EmptyForm()
    if eform.validate_on_submit():
        theclass = Class.query.filter_by(id=classid).first()  # get class with student id
        if theclass is None:
            flash('Class with id "{}" not found.'.format(classid))
            return redirect(url_for('routes.index'))
        current_user.unenroll(theclass) # unenroll student
        db.session.commit() # everytime you change the database, you make a commit
        flash('You are now un-enrolled from class {} {}!'.format(theclass.major, theclass.coursenum))
        return redirect(url_for('routes.index')) #reload, do a redirect to the index route
    else:
        return redirect(url_for('routes.index'))

        