from flask_sqlalchemy import SQLAlchemy
from App.database import db

class CoursePlan(db.Model):

    coursePlanID = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    courseID = db.Column(db.String(30), db.ForeignKey('course.courseID'), nullable=False)
    student = db.relationship('Student', backref=db.backref('course_plan', lazy=True))
    course = db.relationship('Course', backref=db.backref('course_plan', lazy=True))

    def __init__(self, studentID, courseID):
        self.studentID = studentID
        self.courseID = courseID

    def toJSON(self):
        return{
            'coursePlanID' : self.coursePlanID,
            'student' : self.student.toJSON(),
            'course' : self.course.toJSON()
        }