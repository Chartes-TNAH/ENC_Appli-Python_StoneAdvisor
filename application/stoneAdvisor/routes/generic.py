from flask import render_template, url_for, request, flash, redirect
from stoneAdvisor.app import app, login
from stoneAdvisor.modeles.donnees import Sites, Images
from stoneAdvisor.modeles.users import User
from flask_login import login_user, current_user, logout_user

# Sommaire :

# Accueil
# Index des sites archéologiques enregistrés
# Page individuelle des sites archéologiques
# Recherche
# Inscription
# Connexion
# Déconnexion
# Ajout d'un site archéologique dans la base de données
# Modification d'un site archéologique de la base de données
# Suppression d'un site archéologique de la base de données

# Accueil.
@app.route("/")
def accueil():
    sites = Sites.query.all()
    return render_template("pages/accueil.html", nom="Stone Advisor", sites=sites)

# Index des sites archéologiques enregistrés.
@app.route("/sites")
def index():
    sites = Sites.query.all()
    return render_template("pages/notice_sites.html", nom="Stone Advisor", sites=sites)

@app.route("/sites/<int:Id>")
def site(Id):
    site = Sites.query.get(Id)
    image = site.Images
    return render_template("pages/sites.html", nom="Stone Advisor", site=site, image=image)

# Recherche.
@app.route("/recherche")
def recherche():
    motclef = request.args.get("keyword", None)
    #liste vide de résultats
    resultats = []
    #titre par défaut de la page
    titre = "Recherche"
    if motclef:
        resultats = Sites.query.filter(Sites.Nom.like("%{}%".format(motclef))).all()
        titre = 'Résultats pour la recherche "' + motclef + '"'
    return render_template("pages/recherche.html", resultats=resultats, titre=titre)

# Inscription.
@app.route("/inscription", methods=["GET", "POST"])
def inscription():
    # Si on est en POST, cela veut dire que le formulaire a été envoyé
    if request.method == "POST":
        statut, donnees = User.creer(
            login=request.form.get("login", None),
            email=request.form.get("email", None),
            nom=request.form.get("nom", None),
            motdepasse=request.form.get("motdepasse", None)
        )

        if statut is True:
            flash("Enregistrement effectué. Identifiez-vous maintenant", "success")
            return redirect("/")
        else:
            flash("L'ajout de vos données a échoué pour les raisons suivantes : " + ",".join(donnees), "error")
            return render_template("pages/inscription.html")
    else:
        return render_template("pages/inscription.html")

# Connexion.
@app.route("/connexion", methods=["POST", "GET"])
def connexion():
    if current_user.is_authenticated is True:
        flash("Vous êtes déjà connecté-e.", "info")
        return redirect("/")
    # Si on est en POST, cela veut dire que le formulaire a été envoyé
    if request.method == "POST":
        user = User.identification(
            login=request.form.get("login", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if user:
            login_user(user)
            return redirect("/")
        else:
            flash("Les identifiants n'ont pas été reconnus.", "error")

    return render_template("pages/connexion.html")

login.login_view = 'connexion'

from flask_login import logout_user, current_user

# Déconnexion.
@app.route("/deconnexion", methods=["POST", "GET"])
def deconnexion():
    if current_user.is_authenticated is True:
        logout_user()
    flash("Vous êtes déconnecté-e.", "info")
    return redirect("/")

# Ajout d'un site archéologique dans la base de données.
@app.route("/participer", methods=["POST", "GET"])
def creation():
    if current_user.is_authenticated is False:
        flash("Pour ajouter des sites archéologiques dans la base de données, veuillez vous connecter.", "info")
        return redirect("/connexion")
    if request.method == "POST":
        statut, donnees = Sites.creer(
            nom=request.form.get("nom", None),
            adresse=request.form.get("adresse", None),
            latitude=request.form.get("latitude", None),
            longitude=request.form.get("longitude", None),
            description=request.form.get("description", None),
            periode=request.form.get("periode", None)
            #image=request.form.get("image", None)
        )

        if statut is True:
            flash("Les données ont été ajoutées à notre base, merci pour votre participation !", "success")
            return redirect("/participer")
        else:
            flash("L'ajout de vos données a échoué pour les raisons suivantes : " + ", ".join(donnees), "danger")
            return render_template("pages/creation.html")
    else:
        return render_template("pages/creation.html")

# Modification d'un site archéologique de la base de données.
@app.route("/modifier/<int:id>", methods=["POST", "GET"])
def modification(id):
    # On renvoie sur la page html les éléments de l'objet site correspondant à l'identifiant de la route
    if request.method == "GET":
        site_a_modifier = Sites.query.get(id)
        return render_template("pages/modification_site.html", site_a_modifier=site_a_modifier)

    # on récupère les données du formulaire modifié
    else:
        statut, donnees= Sites.modifier(
            id=id,
            nom=request.form.get("nom", None),
            adresse=request.form.get("adresse", None),
            latitude=request.form.get("latitude", None),
            longitude=request.form.get("longitude", None),
            description=request.form.get("description", None),
            periode=request.form.get("periode", None)
        )

        if statut is True:
            flash("Modification réussie !", "success")
            return render_template("pages/notice_sites.html")
        else:
            flash("Les erreurs suivantes ont été rencontrées : " + ",".join(donnees), "danger")
            site_a_modifier = Sites.query.get(id)
            return render_template("pages/modification_site.html", site_a_modifier=site_a_modifier)

# Suppression d'un site archéologique de la base de données.
@app.route("/supprimer/<int:id>", methods=["POST", "GET"])
def suppression(id):
    """Route pour supprimer un site archéologique
    :param id: identifiant numérique du site archéologique
    :return render_template or redirect : redirection vers une nouvelle route
    """
    site_a_supprimer = Sites.query.get(id)
    if request.method == "POST":
        statut, donnees = Sites.supprimer(
            id=id
        )

        # erreur SQLAlchemy qui n'empêche pas la bonne mise en oeuvre de la manipulation.
        detached_error = "sqlalchemy.orm.exc.DetachedInstanceError"
        if detached_error:
            flash("Suppression réussie!", "success")
            return redirect("/")
        elif statut is True:
            flash("Suppression réussie!", "success")
            return redirect("/index")
        else:
            flash("Les erreurs suivantes ont été rencontrées : " + ",".join(donnees), "error")
            return render_template("pages/suppression_site.html", site_a_supprimer=site_a_supprimer)
    else:
        return render_template("pages/suppression_site.html", site_a_supprimer=site_a_supprimer)

