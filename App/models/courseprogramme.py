from flask_sqlalchemy import SQLAlchemy
from App.database import db

class CourseProgramme(db.Model):

    courseProgrammeID = db.Column(db.Integer, primary_key=True)
    courseID = db.Column(db.String(30), db.ForeignKey('course.courseID'), nullable=False)
    programmeID = db.Column(db.String(30), db.ForeignKey('programme.programmeID'), nullable=False)
    course = db.relationship('Course', backref=db.backref('course_programme', lazy=True))
    programme = db.relationship('Programme', backref=db.backref('course_programme', lazy=True))

    def __init__(self, courseID, programmeID):
        self.courseID = courseID
        self.programmeID = programmeID

    def toJSON(self):
        return{
            'courseProgrammeID' : self.courseProgrammeID,
            'course' : self.course.toJSON(),
            'programme' : self.programme.toJSON()
        }