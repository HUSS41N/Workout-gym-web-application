from WTC.core.views import index
from enum import unique
from WTC import db,login_manager
from werkzeug import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(32),unique=True,index=True)
    username = db.Column(db.String(20),unique=True,index=True)
    billing_adress = db.Column(db.String(256),index=True)
    pincode = db.Column(db.Integer(),index=True)
    hash_password = db.Column(db.String(128))

    def __init__(self,email,username,billing_adress,pincode,password):
        self.email = email
        self.username = username
        self.billing_adress = billing_adress
        self.pincode = pincode
        self.hash_password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.hash_password,password)
    
    def __repr__(self):
        #I just Hvae this here.I Dont really know why But maybe to debug anything in future
        return f"Username {{self.username}}"

class WorkoutPlanModel(db.Model):
    __tablename__ = 'workoutplan'
    id = db.Column(db.Integer,primary_key=True)
    add = db.Column(db.String(128),index=True)

    def __init__(self,add):
        self.add = add
    
    def __repr__(self):
        return f' {self.add}'