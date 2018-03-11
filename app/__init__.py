from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "SuperSecretKey"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://info2180-project1:password123@localhost/profilebook"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = 'app/static/profile_photo'
db = SQLAlchemy(app)

allowed_exts = ["jpg", "jpeg", "png"]
bio_path = "app/static/bios"

from app import views