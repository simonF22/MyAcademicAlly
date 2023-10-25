from .user import User
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from App.database import db


class Staff(User, UserMixin):
    __tablename__ = 'staff'

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.set_password(password)
        self.userType = "staff"

    
    def makeCourseAvailable(self, course):
        if course.status == 'Available':
            return True
        try:
            course.status = 'Available'
            db.session.add(course)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
    
    def makeCourseUnavailable(self, course):
        if course.status == 'Unavailable':
            return True
        try:
            course.status = 'Unavailable'
            db.session.add(course)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

    #def updateProgrammeRequirements(self, programme):

    def toJSON(self):
        return{
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'userType': 'staff'
        }
