from flask_sqlalchemy import SQLAlchemy
from App.database import db

class Programme(db.Model):

    programmeID = db.Column(db.String(30), primary_key=True)
    programmeName = db.Column(db.String(120), nullable=False, unique=True)
    faculty = db.Column(db.String(80), nullable=False)
    levelOneCredits =  db.Column(db.Integer, nullable=False)
    advancedLevelCredits =  db.Column(db.Integer, nullable=False)
    foundationCredits =  db.Column(db.Integer, nullable=False)
    totalCredits =  db.Column(db.Integer, nullable=False)
    creditsBreakdown = db.Column(db.String(120), nullable=True)
    courses = db.relationship('CourseProgramme', backref=db.backref('programme', lazy='joined'))

    def __init__(self, programmeID, programmeName, faculty, levelOneCredits, advancedLevelCredits, foundationCredits, totalCredits, creditsBreakdown):
        self.programmeID = programmeID
        self.programmeName = programmeName
        self.faculty = faculty
        self.levelOneCredits = levelOneCredits
        self.advancedLevelCredits = advancedLevelCredits
        self.foundationCredits = foundationCredits
        self.totalCredits = totalCredits
        self.creditsBreakdown = creditsBreakdown

    def toJSON(self):
        return{
            'programmeID' : self.programmeID,
            'programmeName' : self.programmeName,
            'faculty' : self.faculty,
            'levelOneCredits' : self.levelOneCredits,
            'advancedLevelCredits' : self.advancedLevelCredits,
            'foundationCredits' : self.foundationCredits,
            'totalCredits' : self.totalCredits,
            'creditsBreakdown' : self.creditsBreakdown,
            #'courses': [course.toJSON() for course in self.courses]
        }
