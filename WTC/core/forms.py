from flask_wtf import FlaskForm
from wtforms import IntegerField,RadioField,SubmitField
from wtforms.validators import DataRequired

class Bmr(FlaskForm):
    age = IntegerField('AGE',validators=[DataRequired()])
    weight = IntegerField('WEIGHT',validators=[DataRequired()])
    height = IntegerField('HEIGHT',validators=[DataRequired()])
    gender = RadioField('GENDER',choices=[('Male','Male'),('Female','Female')],validators=[DataRequired()])
    submit = SubmitField('CALCULATE')