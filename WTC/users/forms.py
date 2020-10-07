from WTC.models import User
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired,Email,EqualTo, ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('confirm_password',message='Password must match!!')])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired()])
    billing_adress = StringField('Billing Adress',validators=[DataRequired()])
    pincode = IntegerField('Pincode',validators=[DataRequired()])
    submit = SubmitField('Register')

    #check if user already exists with same username or email
    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email Already registered!!')
    
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already Exists!!')


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

class WorkoutPlan(FlaskForm):
    add = StringField('ADD EXCERISES BELOW',validators=[DataRequired()])
    submit = SubmitField('ADD')