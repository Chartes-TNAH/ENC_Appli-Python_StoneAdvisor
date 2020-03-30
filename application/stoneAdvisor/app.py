from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from .constantes import SECRET_KEY

chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")

# instanciation de l'application
app = Flask("Stone Advisor", template_folder=templates, static_folder=statics)

# configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_SitesArcheo'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# configuration du secret
app.config['SECRET_KEY'] = SECRET_KEY

# initiation de l'extension
db = SQLAlchemy(app)

from .routes import accueil, notices_sites, site, recherche, inscription
