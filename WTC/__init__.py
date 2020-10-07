import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

############## <CONFIG> ###############
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

############# <DB & Migrate> ###########
db = SQLAlchemy(app)
Migrate(app,db)

############# <LOGIN MNGR> ##############
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

############# <BLUEPRINT> ##############
from WTC.core.views import core
from WTC.error_handler.handler import error_pages
from WTC.users.views import users

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)