from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from subprocess import call

app = Flask(__name__)
app.config['SECRET_KEY'] = "SuperSecretKey"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://fmnibhaashbxuy:73b8e2e2485adfd45f57da653d63950b88fdcae12202a84f80c7f4c297e9e30a@ec2-23-23-222-184.compute-1.amazonaws.com:5432/d27ig8fpt4ch7r"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password123@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/photo'
db = SQLAlchemy(app)

allowed_exts = ["jpg", "jpeg", "png"]

from app import views