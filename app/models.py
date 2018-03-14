from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    bio = db.Column(db.Text(300))
    created_on = db.Column(db.String(12))
    photo = db.Column(db.String(80))
    
    __tablename__ = "users"
    
    def __init__(self,firstname,lastname,gender,email,location,bio,created_on,photo):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.email = email
        self.location = location
        self.bio = bio
        self.created_on = created_on
        self.photo = photo
    
    def __repr__(self):
        return "User: {0} {1}".format(self.firstname, self.lastname)