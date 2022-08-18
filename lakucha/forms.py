import imp
from flask_wtf import FlaskForm
from wtforms import StringField

class Register(FlaskForm):
    firstname=StringField(label='firstname')
    lastname=StringField(label='lastname')
    email=StringField(label='email')
    password=StringField(label='password')
