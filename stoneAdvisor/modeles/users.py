from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .. app import db, login

db.metadata.clear()
class User(db.Model, UserMixin):
    Id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    Nom = db.Column(db.Text, nullable=False)
    Login = db.Column(db.String(45), nullable=False, unique=True)
    Email = db.Column(db.Text, nullable=False)
    Mdp = db.Column(db.String(64), nullable=False)

    @staticmethod
    def log_in(login, password):
        user = User.query.filter(User.Login == login).first()
        if user and check_password_hash(user.Mdp, password):
            return user
        return None

    @staticmethod
    def sign_in(login, email, name, password):
        errors = []
        if not login:
            errors.append("Login missing")
        if not email:
            errors.append("Email missing")
        if not name:
            errors.append("Name missing")
        # the password must exceed 6 digits
        if not password :
            errors.append("Password missing")
        if len(password) < 6:
            errors.append("The password must contain at least 6 digits")

        # Checking that the account is unique
        uniques = User.query.filter(
            db.or_(User.Email == email, User.Login == login)
        ).count()
        if uniques > 0:
            errors.append("The email or login already exists")

        if len(errors) > 0:
            return False, errors

        # Adding the user to the database
        user = User(
            Nom=name,
            Login=login,
            Email=email,
            Mdp=generate_password_hash(password)
        )

        try:
            db.session.add(user)
            db.session.commit()
            return True, user
        except Exception as e:
            return False, [str(e)]

    def get_id(self):
        # returns the user's id
        return self.Id

    @login.user_loader
    def find_user_from_id(id):
        return User.query.get(int(id))
