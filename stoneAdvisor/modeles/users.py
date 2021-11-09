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
    def log_in(username, password):
        user = User.query.filter(User.Login == username).first()
        if user and check_password_hash(user.Mdp, password):
            return user
        return None

    @staticmethod
    def sign_in(username, email, name, password):
        errors = []
        if not username:
            errors.append("username missing")
        if not email:
            errors.append("email missing")
        if not name:
            errors.append("name missing")
        # the password must exceed 6 digits
        if not password :
            errors.append("password missing")
        if len(password) < 6:
            errors.append("the password must contain at least 6 digits")

        # Checking that the account is unique
        email_count = User.query.filter(
            db.or_(User.Email == email)
        ).count()
        if email_count > 0:
            errors.append("this email already exists")

        username_count = User.query.filter(
            db.or_(User.Login == username)
        ).count()
        if username_count > 0:
            errors.append("this username already exists")

        if len(errors) > 0:
            return False, errors

        # Adding the user to the database
        user = User(
            Nom=name,
            Login=username,
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
