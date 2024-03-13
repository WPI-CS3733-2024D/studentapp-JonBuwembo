from flask import render_template
from app import app, db

@app.errorhandler(404) #file not found error
def not_found_error(error): # shows the contents of the error on the webpage in html template
    return render_template('404error.html'), 404

@app.errorhandler(500) 
def internal_error(error):
    db.session.rollback()
    return render_template('500error.html'), 500