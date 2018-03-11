from app import app, db, bio_path, allowed_exts
from flask import render_template, request, url_for, redirect, flash
from forms import NewProfileForm
from werkzeug.utils import secure_filename
from models import User
from sqlalchemy import exc

from datetime import datetime
import os

@app.route("/")
def home():
    return render_template('home.html')
    
    
@app.route("/profile", methods=["GET", "POST"])
def profile():
    newProfileForm = NewProfileForm()
    
    if request.method == "POST":
        if newProfileForm.validate_on_submit():
            try:
                firstname = newProfileForm.firstname.data
                lastname = newProfileForm.lastname.data
                gender = newProfileForm.gender.data
                email = newProfileForm.email.data
                location = newProfileForm.location.data
                bio = os.path.join(os.getcwd(),bio_path,email+".txt")
                created = str(datetime.now()).split()[0]
                
                photo = newProfileForm.photo.data
                photo_path = os.path.join(os.getcwd(), app.config["UPLOAD_FOLDER"], secure_filename(photo.filename))
                
                user = User(firstname, lastname, gender, email, location, bio, created, photo_path)
                
                db.session.add(user)
                db.session.commit()
                
                write_to(bio, newProfileForm.bio.data)
                photo.save(photo_path)
                
                flash("Profile Added", "success")
                return redirect(url_for("home"))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash("Email address already in use", "danger")
                return render_template("create_new_profile.html", newProfileForm = newProfileForm)
            except Exception as e:
                db.session.rollback()
                flash("Internal Error", "danger")
                return render_template("create_new_profile.html", newProfileForm = newProfileForm)
        
        errors = flash_errors(newProfileForm)
        flash(''.join(error+" " for error in errors), "danger")
    return render_template("create_new_profile.html", newProfileForm = newProfileForm)



def write_to(file_path, data):
    with open(file_path, "w") as stream:
        stream.write(data)
        

    
def flash_errors(form):
    error_list =[]
    for field, errors in form.errors.items():
        for error in errors:
            error_list.append(field+": "+error)
            
    return error_list
    
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404