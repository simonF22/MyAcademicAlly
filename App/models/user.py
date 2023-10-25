from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from App.database import db

class User(db.Model, UserMixin):
    
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    email =  db.Column(db.String, nullable=False, unique=True)
    name =  db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    userType =  db.Column(db.String(120), nullable=False)

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.set_password(password)

    def __repr__(self):
        return f'<User {self.id} {self.email} {self.name} {self.userType}>'

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    
    def toJSON(self):
        return{
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'userType': self.userType
        }

