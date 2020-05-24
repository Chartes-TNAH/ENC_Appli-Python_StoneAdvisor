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
    def creer(nom, adresse, latitude, longitude, description, periode):
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
        if not periode:
            erreurs.append("Indiquez une fourchette chronologique")

        # S'il y a au moins une erreur.
        if len(erreurs) > 0:
            return False, erreurs

        # S'il n'y a pas d'erreur, on crée le site.
        site = Sites(
            Nom=nom,
            Adresse=adresse,
            Latitude=latitude,
            Longitude=longitude,
            Description=description,
            Periode=periode,
            #Images=image
        )

        try:
            # On l'ajoute au transport vers la base de données.
            db.session.add(site)
            # On envoie le paquet.
            db.session.commit()

            # On renvoie les informations du site.
            return True, site
        except Exception as erreur:
            return False, [str(erreur)]

    @staticmethod
    def modifier(id, nom, adresse, latitude, longitude, description, periode):
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
        if not periode:
            erreurs.append("Indiquez la fourchette chronologique du site")

        # S'il y a au moins une erreur.
        if len(erreurs) > 0:
            return False, erreurs

        # On récupère un site dans la base.
        site = Sites.query.get(id)

        # On vérifie que l'utilisateur-ice modifie au moins un champ.
        if site.Nom == nom \
                and site.Adresse == adresse \
                and site.Latitude == latitude \
                and site.Longitude == longitude \
                and site.Description == description \
                and site.Periode == periode:
            erreurs.append("Aucune modification n'a été réalisée")

        if len(erreurs) > 0:
            return False, erreurs

        else:
            # Mise à jour du site
            site.Nom = nom
            site.Adresse = adresse
            site.Latitude = latitude
            site.Longitude = longitude
            site.Description = description
            site.Periode = periode

        try:
            # On l'ajoute au transport vers la base de données.
            db.session.add(site)
            # On envoie le paquet.
            db.session.commit()

            # On renvoie les informations du site.
            return True, site
        except Exception as erreur:
            return False, [str(erreur)]

    @staticmethod
    def supprimer(id):
        # :returns: booleen

        site = Sites.query.get(id)

        site.Id = id

        try:
            db.session.delete(site)
            db.session.commit()
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


