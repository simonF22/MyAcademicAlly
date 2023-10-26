from App.database import db
from App.models import User, Staff, Student, Course, Programme

def create_course(courseID, courseName, type, credits, semester, prerequisite=None):
    newCourse = Course(courseID=courseID, courseName=courseName, type=type, credits=credits, semester=semester, prerequisite=prerequisite)
    db.session.add(newCourse)
    db.session.commit()
    return newCourse

def get_course(courseID):
    return Course.query.get(courseID)

def get_all_courses():
    return Course.query.all()

def get_available_courses():
    return Course.query.filter_by(status='Available').all()

def get_all_courses_json():
    courses = Course.query.all()
    if courses:
        return [course.toJSON() for course in courses]
    return []

def get_available_courses_json():
    courses = Course.query.filter_by(status='Available').all()
    if courses:
        return [course.toJSON() for course in courses]
    return []

def make_course_available(staff, course):
    return staff.makeCourseAvailable(course)

def make_course_unavailable(staff, course):
    return staff.makeCourseUnavailable(course)
