from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from .constantes import SECRET_KEY
# plugin permettant la gestion des utilisateur-ice-s
# ce plugin se souvient de l'activité utilisatrice
from flask_login import LoginManager

chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")

# instanciation de l'application
app = Flask("Stone Advisor", template_folder=templates, static_folder=statics)

# Mise en place de la gestion d'utilisateur-rice-s
login = LoginManager(app)

# configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_SitesArcheo'

# configuration du secret
app.config['SECRET_KEY'] = SECRET_KEY

# initiation de l'extension
db = SQLAlchemy(app)

from .routes import accueil, notices_sites, site, recherche, inscription
