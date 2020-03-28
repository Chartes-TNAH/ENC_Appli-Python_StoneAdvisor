from flask import render_template, url_for, request
from .app import app
from .modeles.donnees import Sites, Images
from .modeles.users import User
from flask import flash, redirect, request

# page d'accueil.
@app.route("/")
def accueil():
    sites = Sites.query.all()
    return render_template("pages/accueil.html", nom="Stone Advisor")

# page de la liste des sites archéologiques enregistrés.
@app.route("/sites")
def notices_sites():
    sites = Sites.query.all()
    return render_template("pages/notice_sites.html", nom="Stone Advisor", sites=sites)

# page des sites individuels enregistrés.
@app.route("/sites/<int:Id>")
def site(Id):
    site = Sites.query.get(Id)
    image = site.Images
    return render_template("pages/sites.html", nom="Stone Advisor", site=site, image=image)

# page de recherche.
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

# page d'inscription.
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
            flash("Les erreurs suivantes ont été rencontrées : " + ",".join(donnees), "error")
            return render_template("pages/inscription.html")
    else:
        return render_template("pages/inscription.html")