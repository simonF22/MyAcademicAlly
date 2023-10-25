from flask_sqlalchemy import SQLAlchemy
from App.database import db

class CourseProgramme(db.Model):

    courseProgrammeID = db.Column(db.Integer, primary_key=True)
    courseID = db.Column(db.String(30), db.ForeignKey('course.courseID'), nullable=False)
    programmeID = db.Column(db.String(30), db.ForeignKey('programme.programmeID'), nullable=False)

    def __init__(self, courseID, programmeID):
        self.courseID = courseID
        self.programmeID = programmeID

    def toJSON(self):
        return{
            'courseProgrammeID' : self.courseProgrammeID,
            'course' : self.courseID,
            'programme' : self.programmeID
        }