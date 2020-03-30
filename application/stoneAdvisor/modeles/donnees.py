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

    @staticmethod
    def creer(nom, adresse, latitude, longitude, description):
        erreurs = []
        if not nom:
            erreurs.append("Insérez un nom de site")
        if not adresse:
            erreurs.append("Insérez une adresse")
        if not latitude:
            erreurs.append("Insérez une latitude")
        if not longitude:
            erreurs.append("Insérez une longitude")
        if not description:
            erreurs.append("Insérez une description de quelques lignes")

        # S'il y a au moins une erreur.
        if len(erreurs) > 0:
            return False, erreurs

        # S'il n'y a pas d'erreur, on crée le site.
        site = Sites(
            Nom=nom,
            Adresse=adresse,
            Latitude=latitude,
            Longitude=longitude,
            Description=description
        )

        try:
            # On l'ajoute au transport vers la base de données.
            db.session.add(site)
            # On envoie le paquet.
            db.session.commit()

            # On renvoie le site.
            return True, site
        except Exception as erreur:
            return False, [str(erreur)]

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


