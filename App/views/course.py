from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user

from App.controllers import (
    get_all_courses_json,
    get_available_courses_json,
    get_staff,
    get_student,
    get_course,
    make_course_available,
    make_course_unavailable,
    create_CourseHistory,
    remove_CourseHistory,
    get_coursehistory,
    get_coursehistory_by_student_json,
    create_CoursePlan,
    remove_CoursePlan,
    get_courseplan,
    get_courseplan_by_student_json
)

course_views = Blueprint('course_views', __name__, template_folder='../templates')

@course_views.route('/courses', methods=['GET'])
@jwt_required()
def get_all_courses_action():
    staff = get_staff(jwt_current_user.id)
    if staff:
        courses = get_all_courses_json()
        return jsonify(courses)
    return jsonify({"error": "cannot perform that action"}), 403
     


@course_views.route('/availablecourses', methods=['GET'])
@jwt_required()
def get_available_courses_action():
    courses = get_available_courses_json()
    return jsonify(courses)


@course_views.route('/courses/<string:courseID>', methods=['PUT'])
@jwt_required()
def toggle_course_availablity_action(courseID):
    staff = get_staff(jwt_current_user.id)
    course = get_course(courseID)
    if staff:
        if course:
            if course.status == 'Available':
                make_course_unavailable(staff, course)
                return jsonify({"message": f"course {course.courseID} is now unavailable"}), 200
            else:
                make_course_available(staff, course)
                return jsonify({"message": f"course {course.courseID} is now available"}), 200
        return jsonify({"error": "invalid course id"}), 400
    return jsonify({"error": "cannot perform that action"}), 403


@course_views.route('/coursehistory', methods=['GET'])
@jwt_required()
def get_course_history():
    studentid = jwt_current_user.id
    return get_coursehistory_by_student_json(studentid)


@course_views.route('/coursehistory', methods=['POST'])
@jwt_required()
def add_course_to_history():
    student = get_student(jwt_current_user.id)
    data = request.json
    courseID = data['courseID']
    course = get_course(courseID)
    if course:
        coursehistory = create_CourseHistory(student, courseID)
        return jsonify({"message": "course added to student course history"}), 201
    return jsonify ({"error" : "invalid course id"}), 400


@course_views.route('/coursehistory/<string:courseID>', methods=['DELETE'])
@jwt_required()
def remove_course_from_history(courseID):
    student = get_student(jwt_current_user.id)
    course = get_course(courseID)
    if course:
        courseHistoryToRemove = get_coursehistory(student.id, courseID)
        if courseHistoryToRemove:
            if remove_CourseHistory(student, courseHistoryToRemove):
                return jsonify({"message" : "course removed from student course history"}), 200
        return jsonify ({"error" : "course does not exist in student course history"}), 400
    return jsonify ({"error" : "invalid course id"}), 400


@course_views.route('/courseplan', methods=['GET'])
@jwt_required()
def get_course_plan():
    studentid = jwt_current_user.id
    return get_courseplan_by_student_json(studentid)


@course_views.route('/courseplan', methods=['POST'])
@jwt_required()
def add_course_to_plan():
    student = get_student(jwt_current_user.id)
    data = request.json
    courseID = data['courseID']
    course = get_course(courseID)
    if course:
        courseplan = create_CoursePlan(student, courseID)
        return jsonify({"message": "course added to student course plan"}), 201
    return jsonify ({"error" : "invalid course id"}), 400


@course_views.route('/courseplan/<string:courseID>', methods=['DELETE'])
@jwt_required()
def remove_course_from_plan(courseID):
    student = get_student(jwt_current_user.id)
    course = get_course(courseID)
    if course:
        coursePlanToRemove = get_courseplan(student.id, courseID)
        if coursePlanToRemove:
            if remove_CoursePlan(student, coursePlanToRemove):
                return jsonify({"message" : "course removed from student course plan"}), 200
        return jsonify ({"error" : "course does not exist in student course plan"}), 400
    return jsonify ({"error" : "invalid course id"}), 400