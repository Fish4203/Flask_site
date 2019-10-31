from flask_app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_app import login

class User(UserMixin,   db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64), index=True, unique=True)
    Email = db.Column(db.String(120), index=True, unique=True)
    Pass_Hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    def gen_pass(self, Pass_Hash):
        self.Pass_Hash = generate_password_hash(Pass_Hash)

    def check_pass(self, Pass_Hash):
        return check_password_hash(self.Pass_Hash , Pass_Hash)

    def __repr__(self):
        return '<User {}>'.format(self.Name)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String())
    Body = db.Column(db.String())
    User = db.Column(db.Integer, db.ForeignKey('user.id'))
    Time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Post {}>'.format(self.Body)
        #return self.Body

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
