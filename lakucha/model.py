import email
from email.policy import default
from lakucha import db

class User(db.Model):
   id=db.Column(db.Integer(), primary_key=True)
   firstname=db.Column(db.String(length=50), nullable=False, unique=True)
   lastnamename=db.Column(db.String(length=50), nullable=False, unique=True)
   email=db.Column(db.String(length=50), nullable=False, unique=True)
   password=db.Column(db.String(length=50), nullable=False, default=1000)
   
class Foods(db.Model):
   id=db.Column(db.Integer(), primary_key=True)
   name=db.Column(db.String(length=50), nullable=False, unique=True)
   price=db.Column(db.Integer(), nullable=True, unique=True)
   description=db.Column(db.Integer(), nullable=True, unique=True)

def __repr__(self):
   return f'Foods {self.name}'
