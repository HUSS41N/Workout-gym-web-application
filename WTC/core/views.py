import math
from flask import render_template,Blueprint,redirect,url_for,session
from WTC.contact.forms import ContactUs
from WTC.core.forms import Bmr
from flask_login import login_required
core = Blueprint('core',__name__)


@core.route('/')
def index():
    form = ContactUs()
    return render_template('index.html',form=form)

@core.route('/bmr',methods=['GET','POST'])
@login_required
def bmr():
    form = Bmr()
    if form.validate_on_submit():
        session['age'] = form.age.data
        session['weight'] = form.weight.data
        session['height'] = form.height.data
        session['gender'] = form.gender.data 
        if session['gender'] == 'Male':
            bmr = 66.47 + (13.75 * session['weight'] ) + (5.003 * session['height']  ) - (6.755 * session['age'] )
            return render_template('bmr.html',bmr=(math.floor(bmr)),form=form)
        elif session['gender'] == 'Female':
            bmr =  655.1 + (9.563 * session['weight'] ) + (1.85 * session['height'] ) - (4.676 * session['age'])
            return render_template('bmr.html',bmr=(math.floor(bmr)),form=form)
    return render_template('bmr.html',form=form)

