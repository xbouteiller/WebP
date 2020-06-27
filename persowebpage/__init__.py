# puppycompanyblog/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

#####################################################
# db
# basedir = os.path.abspath(os.path.dirname(__file__))
#
# app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
# Migrate(app, db)

#####################################################
# LoginManager

# login_manager = LoginManager()
#
# login_manager.init_app(app)
# login_manager.login_view  = 'users.login'

#####################################################

from persowebpage.core.views import core
from persowebpage.error_pages.handlers import error_pages
from persowebpage.method.views import method
from persowebpage.publication.views import publication
from persowebpage.research.views import research
from persowebpage.teaching.views import teaching

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(method)
app.register_blueprint(publication)
app.register_blueprint(research)
app.register_blueprint(teaching)
