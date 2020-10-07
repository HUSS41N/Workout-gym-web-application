from ast import Str
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Email

class ContactUs(FlaskForm):
    fullname = StringField('FULL NAME',validators=[DataRequired()])
    email = StringField('EMAIL',validators=[DataRequired(),Email()])
    message = TextAreaField('MESSAGE',validators=[DataRequired()])
    submit = SubmitField('SEND MESSAGE')