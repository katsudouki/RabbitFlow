from extensions import db 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import models

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


def create_admin():
    admin = User.query.filter_by(username="admin").first()
    if not admin:
        hashed_password = generate_password_hash("admin", method="pbkdf2:sha256")
        new_admin = User(username="admin", password=hashed_password)
        db.session.add(new_admin)
        db.session.commit()
        print("Admin user created.")
    else:
        print("Admin user already exists.")
from app import app  
with app.app_context():
    db.create_all()
    create_admin()
