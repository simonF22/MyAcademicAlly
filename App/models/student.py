from .user import User
from .coursehistory import CourseHistory
from .courseplan import CoursePlan
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from App.database import db

class Student(User, UserMixin):
    __tablename__ = 'student'

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.set_password(password)
        self.userType = "student"

    def selectPastCourse(self, courseID):
        newCourseHistory = CourseHistory(self.id, courseID)
        try:
            db.session.add(newCourseHistory)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
    
    def deletePastCourse(self, courseHistory):
        try:
            db.session.delete(courseHistory)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

    def selectPlannedCourse(self, courseID):
        newCoursePlan = CoursePlan(self.id, courseID)
        try:
            db.session.add(newCoursePlan)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
    
    def deletePlannedCourse(self, coursePlan):
        try:
            db.session.delete(coursePlan)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

    def toJSON(self):
        return{
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'userType': 'student'
        }