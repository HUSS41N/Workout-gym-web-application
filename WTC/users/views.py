from flask import render_template,redirect,url_for,Blueprint,flash,abort,request
from WTC.users.forms import RegistrationForm,LoginForm,WorkoutPlan
from WTC import db
from flask_login import login_user,login_required,logout_user,current_user
from WTC.models import User,WorkoutPlanModel

users = Blueprint('users',__name__)

@users.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,
                    billing_adress=form.billing_adress.data,pincode=form.pincode.data,
                    password=form.password.data )
        db.session.add(user)
        db.session.commit()
        flash('Thank you for Registring with us')
        return redirect(url_for('users.login'))
    return render_template('register.html',form=form)

@users.route('/login',methods=['GET','POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
       user = User.query.filter_by(email=form.email.data).first()

       if user.check_password(form.password.data) and user is not None:
           login_user(user)
           flash('You are Logged in Successfully!')
            #If user is trying to acces some page where login in required
           next = request.args.get('next')
           if next == None or not next[0] == '/':
               next = url_for('core.index')
           return redirect(next)
   return render_template('login.html',form=form)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out!')
    return redirect(url_for('core.index'))

@users.route('/<username>/make-workout-routine',methods=['GET','POST'])
@login_required
def workoutplan(username):
    
    

    form = WorkoutPlan()

    if form.validate_on_submit():
        add = WorkoutPlanModel(add=form.add.data,user_id=current_user.id)
        db.session.add(add)
        db.session.commit()
        flash('Workout Added')
        return redirect(url_for('users.workoutplan',username=username, **request.args))
    #grabbing all the added workouts to display them on template
    user = User.query.filter_by(username=username).first_or_404()
    addedexcerise_db = WorkoutPlanModel.query.filter_by(user_added_workout=user)

    return render_template('workout_plan.html',form=form,addedexcerise_db=addedexcerise_db,user=user)


@users.route('/<int:workoutplan_id>/delete',methods=['GET','POST'])
def delete(workoutplan_id):
    delete_excerise = WorkoutPlanModel.query.get_or_404(workoutplan_id)
    db.session.delete(delete_excerise)
    db.session.commit()
    username=current_user.username
    return redirect(url_for('users.workoutplan',username=username, **request.args))

@users.route('/profile')
@login_required
def profile():
    return render_template('profile.html')