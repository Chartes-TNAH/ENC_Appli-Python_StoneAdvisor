from .. app import db

class Sites(db.Model):
    Id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    Nom = db.Column(db.Text, nullable=False)
    Adresse = db.Column(db.Text, nullable=False)
    Latitude = db.Column(db.Integer, nullable=False)
    Longitude = db.Column(db.Integer, nullable=False)
    Description = db.Column(db.Text)
    Periode = db.Column(db.Integer)
    Lien = db.Column(db.Text)
    Images = db.relationship('Images', backref='site')

class Images(db.Model):
    Id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    Source = db.Column(db.Text, nullable=False)
    Image = db.Column(db.Text, nullable=False)
    IdSite = db.Column(db.Integer, db.ForeignKey('sites.Id'))
    Legende = db.Column(db.Text)

class User(db.Model):
    Id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    Nom = db.Column(db.Text, nullable=False)
    Login = db.Column(db.String(45), nullable=False, unique=True)
    Email = db.Column(db.Text, nullable=False)
    Mdp = db.Column(db.String(64), nullable=False)


