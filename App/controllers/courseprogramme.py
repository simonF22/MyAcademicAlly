from App.database import db
from App.models import User, Student, Staff, Course, Programme, CourseProgramme


def create_course_programme(courseID, programmeID):
    newCourseProgramme = CourseProgramme(courseID, programmeID)
    db.session.add(newCourseProgramme)
    db.session.commit()
    return newCourseProgramme

def get_course_programme_by_courseid(courseID): 
    return CourseProgramme.query.filter_by(courseID=courseID).all()

def get_course_programme_by_programmeid(programmeID): 
    return CourseProgramme.query.filter_by(programmeID=programmeID).all()

def get_all_course_programme():
    return CourseProgramme.query.all()

def get_all_course_programme_json():
    courseprogramme = CourseProgramme.query.all()
    if courseprogramme:
        return [courseprogramme.toJSON() for cp in courseprogramme]
    return []