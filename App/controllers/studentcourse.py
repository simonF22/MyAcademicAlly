from App.database import db
from App.models import User, Student, Staff, Course, Programme, CourseHistory, CoursePlan


''' CONTROLLERS FOR COURSE HISTORY'''

def create_CourseHistory(student, courseID):
    return student.selectPastCourse(courseID)

def remove_CourseHistory(student, courseHistory):
    return student.deletePastCourse(courseHistory)

def get_coursehistory(studentID, courseID):
    return CourseHistory.query.filter_by(studentID=studentID, courseID=courseID).first()

def get_coursehistory_by_student(studentID): 
    return CourseHistory.query.filter_by(studentID=studentID).all()

def get_coursehistory_by_student_json(studentID): 
    coursehistory = CourseHistory.query.filter_by(studentID=studentID).all()
    if coursehistory:
        return [ch.toJSON() for ch in coursehistory]
    return []

def get_all_coursehistory():
    return CourseHistory.query.all()

def get_all_coursehistory_json():
    coursehistory = CourseHistory.query.all()
    if coursehistory:
        return [ch.toJSON() for ch in coursehistory]
    return []

''' CONTROLLERS FOR COURSE PLAN'''

def create_CoursePlan(student, courseID):
    return student.selectPlannedCourse(courseID)

def remove_CoursePlan(student, coursePlan):
    return student.deletePlannedCourse(coursePlan)

def get_courseplan(studentID, courseID):
    return CoursePlan.query.filter_by(studentID=studentID, courseID=courseID).first()

def get_courseplan_by_student(studentID):
    return CoursePlan.query.filter_by(studentID=studentID).all()

def get_courseplan_by_student_json(studentID):
    courseplans = CoursePlan.query.filter_by(studentID=studentID).all()
    if courseplans:
        return [courseplan.toJSON() for courseplan in courseplans]
    return []

def get_all_courseplans():
    return CoursePlan.query.all()

def get_all_courseplans_json():
    courseplans = CoursePlan.query.all()
    if courseplans:
        return [courseplan.toJSON() for courseplan in courseplans]
    return []
