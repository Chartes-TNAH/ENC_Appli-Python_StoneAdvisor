from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
#from .constantes import SECRET_KEY
#from flask_login import LoginManager

current_dir = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(current_dir, "templates")
statics = os.path.join(current_dir, "static")

app = Flask("Stone Advisor", template_folder=templates, static_folder=statics)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_SitesArcheo'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

#app.config['SECRET_KEY'] = SECRET_KEY

#login = LoginManager(app)

from .routes import generic, error
