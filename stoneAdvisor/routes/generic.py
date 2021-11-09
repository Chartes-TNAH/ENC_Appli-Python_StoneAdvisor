from flask import render_template, url_for, request, flash, redirect
from stoneAdvisor.app import app, login
from stoneAdvisor.modeles.donnees import Sites, Images
from stoneAdvisor.modeles.users import User
from flask_login import login_user, current_user, logout_user

# Home
@app.route("/")
def home():
    sites = Sites.query.all()
    return render_template("pages/home.html", sites=sites)


# Index of archaeological sites
@app.route("/index")
def index():
    sites = Sites.query.all()
    return render_template("pages/index.html", nom="Stone Advisor", sites=sites)


# Individual site page
# Needs an ID
@app.route("/index/<int:Id>")
def site(Id):
    site = Sites.query.get(Id)
    image = site.Images
    return render_template("pages/site_page.html", nom="Stone Advisor", site=site, image=image)

# Search bar
@app.route("/search")
def search():
    keyword = request.args.get("keyword", None)
    results = []
    title = "Search"
    if keyword:
        # Looking for the searched words in the database
        results = Sites.query.filter(Sites.Nom.like("%{}%".format(keyword))).all()
        # Results
        title = 'Results for "' + keyword + '"'
    return render_template("pages/search.html", results=results, title=title)

# Signing in
@app.route("/signin", methods=["GET", "POST"])
def sign_in():
    # Registration form
    if request.method == "POST":
        status, data = User.sign_in(
            username=request.form.get("username", None),
            email=request.form.get("email", None),
            name=request.form.get("name", None),
            password=request.form.get("password", None)
        )

        if status is True:
            flash("You are now registered and can log in.", "success")
            return redirect("/")
        else:
            flash("Error : " + ", ".join(data), "error")
            return render_template("pages/signin.html")
    else:
        return render_template("pages/signin.html")

# Logging in
@app.route("/login", methods=["POST", "GET"])
def log_in():
    if current_user.is_authenticated is True:
        flash("You are already logged in", "info")
        return redirect("/")
    if request.method == "POST":
        user = User.log_in(
            username=request.form.get("username", None),
            password=request.form.get("password", None)
        )
        if user:
            login_user(user)
            return redirect("/")
        else:
            flash("The information wasn't recognised", "error")

    return render_template("pages/login.html")

login.login_view = 'login'


# Logging out
@app.route("/logout", methods=["POST", "GET"])
def log_out():
    if current_user.is_authenticated is True:
        logout_user()
    flash("You are logged out", "info")
    return redirect("/")

# Adding an archaeological site to the database
@app.route("/contribute", methods=["POST", "GET"])
def creation():
    # if the user isn't logged in
    if current_user.is_authenticated is False:
        flash("To contribute, log in or sign in", "info")
        return redirect("/login")
    # logging in 
    if request.method == "POST":
        # on appelle la staticmethod "creer" du fichier "modeles.data.py".
        status, data = Sites.creer(
            nom=request.form.get("name", None),
            adresse=request.form.get("address", None),
            latitude=request.form.get("latitude", None),
            longitude=request.form.get("longitude", None),
            description=request.form.get("description", None)
        )

        if status is True:
            flash("Thank you for your contribution!", "success")
            return redirect("/index")
        else:
            # displaying the errors
            flash("Error: " + ", ".join(data), "error")
            return render_template("pages/creation.html")
    else:
        return render_template("pages/creation.html")


# Edit one of the archaeological sites
@app.route("/edit/<int:Id>", methods=["POST", "GET"])
def edit(Id):
    # to edit a website, enter its "id" in the route
    # This displays the editing form
    if request.method == "GET":
        site_to_edit = Sites.query.get(Id)
        return render_template("pages/edit.html", site_to_edit=site_to_edit)

    # sending the data inserting in the form to the database
    else:
        status, data= Sites.edit(
            id=Id,
            nom=request.form.get("nom", None),
            adresse=request.form.get("adresse", None),
            latitude=request.form.get("latitude", None),
            longitude=request.form.get("longitude", None),
            description=request.form.get("description", None),
            #periode=request.form.get("periode", None)
        )

        if status is True:
            flash("Edit successful !", "success")
            return render_template("pages/index.html")
        else:
            # Errors
            flash("Errors: " + ",".join(data), "error")
            site_a_modifier = Sites.query.get(Id)
            return render_template("pages/edit.html", site_to_edit=site_to_edit)

# Delete an archaeological site
# to delete a website, enter its "id" in the route
@app.route("/delete/<int:Id>", methods=["POST", "GET"])
def delete(Id):
    site_to_delete = Sites.query.get(Id)
    if request.method == "POST":
        status, data = Sites.delete(
            id=Id
        )

        # ignore SQLAlchemy error
        detached_error = "sqlalchemy.orm.exc.DetachedInstanceError"
        if detached_error:
            flash("Delete successful!", "success")
            return redirect("/")
        elif status is True:
            flash("Delete successful!", "success")
            return redirect("/index")
        else:
            # errors
            flash("Errors : " + ",".join(data), "error")
            return render_template("pages/delete.html", site_to_delete=site_to_delete)
    else:
        return render_template("pages/delete.html", site_to_delete=site_to_delete)

