from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize SQLAlchemy
db = SQLAlchemy()

# User model for 'accounts' table
class User(UserMixin, db.Model):
    __tablename__ = 'accounts'
    acc_id = db.Column(db.Integer, primary_key=True)
    acc_name = db.Column(db.String(80), nullable=False)
    acc_password_hash = db.Column(db.String(128), nullable=False)
    acc_email = db.Column(db.String(120), unique=True, nullable=False)
    creation_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    active = db.Column(db.Boolean, default=True)

    # Method to check hashed password
    def check_password(self, password):
        return check_password_hash(self.acc_password_hash, password)
