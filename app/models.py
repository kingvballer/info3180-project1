from . import db

class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String, unique=True)
    firstname = db.Column(db.String(80), unique=True)
    lastname = db.Column(db.String(120), unique=True)
    age = db.Column(db.Integer(3), unique=True)
    sex = db.column(db.String(10), unique=True)

    def __init__(self, userid, image, firstname, lastname, age, sex):
        self.userid = userid
        self.image = image
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex

    def __repr__(self):
        return '<User %r>' % self.username