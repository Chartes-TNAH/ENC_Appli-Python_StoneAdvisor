from flask import Flask
# une application Flask est une instanciation de la classe Flask, que l'on commence par importer.
from flask_sqlalchemy import SQLAlchemy
import os
# le module OS de Python permet d'utiliser les fonctionnalités du système d'exploitation sur lequel s'exécute python.
from .constantes import SECRET_KEY
# import de la clé secrète pour le mot de passe des sessions utilisatrices
from flask_login import LoginManager
# plugin permettant la gestion des utilisateur-ice-s
# ce plugin se souvient de l'activité des utilisateur-ice-s

# le module os permet d'indiquer un chemin à n'importe quel système d'exploitation sur lequel s'exécute python.
# il indique ici les chemins des dossiers de templates et d'images (statics). 
chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")

# instanciation de l'application
app = Flask("Stone Advisor", template_folder=templates, static_folder=statics)

# mise en place de la gestion d'utilisateur-rice-s
login = LoginManager(app)

# configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_SitesArcheo'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# configuration du secret
app.config['SECRET_KEY'] = SECRET_KEY

# initiation de l'extension
db = SQLAlchemy(app)

# import des chemins généraux (page d'accueil, page de connexion...) et les chemins des pages d'erreur.
from .routes import generic, error
