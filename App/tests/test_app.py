import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import User, Staff, Student, Course, Programme, CourseProgramme, CourseHistory, CoursePlan
from App.controllers import (
    create_staff, create_student, create_course,
    get_staff, get_student, get_all_users_json, get_course, get_coursehistory,
    login_staff, login_student,
    update_staff, update_student
)


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):
    # pure function no side effects or integrations called

    def test_new_staff_user(self):
        newstaff = Staff("bob@uwimail.com", "bob", "bobpass")
        assert newstaff.email == "bob@uwimail.com"

    def test_new_student_user(self):
        newstudent = Student("jane@uwimail.com", "jane", "janepass")
        assert newstudent.email == "jane@uwimail.com"

    def test_staffJSON(self):
        staff = Staff("bob@uwimail.com", "bob", "bobpass")
        staff_json = staff.toJSON()
        self.assertDictEqual(staff_json, {
            "id":None, 
            "email":"bob@uwimail.com", 
            "name":"bob", 
            "userType":"staff"
        })

    def test_studentJSON(self):
        student = Student("jane@uwimail.com", "jane", "janepass")
        student_json = student.toJSON()
        self.assertDictEqual(student_json, {
            "id":None, 
            "email":"jane@uwimail.com", 
            "name":"jane", 
            "userType":"student"
        })

    def test_staff_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        staff = Staff("bob@uwimail.com", "bob", password)
        assert staff.password != password

    def test_student_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        student = Student("jane@uwimail.com", "jane", password)
        assert student.password != password

    def test_staff_check_password(self):
        password = "mypass"
        staff = Staff("bob@uwimail.com", "bob", password)
        assert staff.check_password(password)

    def test_student_check_password(self):
        password = "mypass"
        student = Student("jane@uwimail.com", "jane", password)
        assert student.check_password(password)

    def test_new_course(self):
        newcourse = Course("COMP1601", "Computer Programming I", "Level I", 3, 1)
        assert newcourse.courseID == "COMP1601"
    
    def test_courseJSON(self):
        course = Course("COMP1601", "Computer Programming I", "Level I", 3, 1)
        course_json = course.toJSON()
        self.assertDictEqual(course_json, {
            "courseID":"COMP1601", 
            "courseName":"Computer Programming I", 
            "type":"Level I", 
            "credits":3,
            "semester":1,
            "prerequisite":None,
            "status":"Unavailable"
        })

    def test_new_programme(self):
        newprogramme = Programme("CS_Spec", "BSc Computer Science (Special)", "FST", 24, 60, 9, 93, "Level One: 24 Core Credits | Advanced Level: 60 Credits (45 Core Credits + 15 Elective Credits) | Foundation: 9 Credits")
        assert newprogramme.programmeID == "CS_Spec"
    
    def test_programmeJSON(self):
        programme = Programme("CS_Spec", "BSc Computer Science (Special)", "FST", 24, 60, 9, 93, "Level One: 24 Core Credits | Advanced Level: 60 Credits (45 Core Credits + 15 Elective Credits) | Foundation: 9 Credits")
        programme_json = programme.toJSON()
        self.assertDictEqual(programme_json, {
            "programmeID":"CS_Spec", 
            "programmeName":"BSc Computer Science (Special)", 
            "faculty":"FST", 
            "levelOneCredits":24,
            "advancedLevelCredits":60,
            "foundationCredits":9,
            "totalCredits":93,
            "creditsBreakdown":"Level One: 24 Core Credits | Advanced Level: 60 Credits (45 Core Credits + 15 Elective Credits) | Foundation: 9 Credits"
        })

    def test_new_courseprogramme(self):
        course = Course("COMP1601", "Computer Programming I", "Level I", 3, 1)
        programme = Programme("CS_Spec", "BSc Computer Science (Special)", "FST", 24, 60, 9, 93, "Level One: 24 Core Credits | Advanced Level: 60 Credits (45 Core Credits + 15 Elective Credits) | Foundation: 9 Credits")
        newCourseProgramme = CourseProgramme(course.courseID, programme.programmeID)
        assert newCourseProgramme.courseID == "COMP1601" and newCourseProgramme.programmeID == "CS_Spec"

    def test_courseprogrammeJSON(self):
        course = Course("COMP1601", "Computer Programming I", "Level I", 3, 1)
        programme = Programme("CS_Spec", "BSc Computer Science (Special)", "FST", 24, 60, 9, 93, "Level One: 24 Core Credits | Advanced Level: 60 Credits (45 Core Credits + 15 Elective Credits) | Foundation: 9 Credits")
        courseprogramme = CourseProgramme(course.courseID, programme.programmeID)
        courseprogramme.course = course
        courseprogramme.programme = programme
        courseprogramme_json = courseprogramme.toJSON()
        self.assertDictEqual(courseprogramme_json, {
            "courseProgrammeID":None,
            "course":{
                "courseID":"COMP1601", 
                "courseName":"Computer Programming I", 
                "type":"Level I", 
                "credits":3,
                "semester":1,
                "prerequisite":None,
                "status":"Unavailable"
            },
            "programme":{
                "programmeID":"CS_Spec", 
                "programmeName":"BSc Computer Science (Special)", 
                "faculty":"FST", 
                "levelOneCredits":24,
                "advancedLevelCredits":60,
                "foundationCredits":9,
                "totalCredits":93,
                "creditsBreakdown":"Level One: 24 Core Credits | Advanced Level: 60 Credits (45 Core Credits + 15 Elective Credits) | Foundation: 9 Credits"
            }
        })

    def test_new_coursehistory(self):
        student = Student("jane@uwimail.com", "jane", "janepass")
        student.id = 1
        course = Course("COMP1601", "Computer Programming I", "Level I", 3, 1)
        newCourseHistory = CourseHistory(student.id, course.courseID)
        assert newCourseHistory.studentID == 1 and newCourseHistory.courseID == "COMP1601"

    def test_coursehistoryJSON(self):
        student = Student("jane@uwimail.com", "jane", "janepass")
        student.id = 1
        course = Course("COMP1601", "Computer Programming I", "Level I", 3, 1)
        coursehistory = CourseHistory(student.id, course.courseID)
        coursehistory.student = student
        coursehistory.course = course
        coursehistory_json = coursehistory.toJSON()
        self.assertDictEqual(coursehistory_json, {
            "courseHistoryID":None,
            "student":{
                "id":1, 
                "email":"jane@uwimail.com", 
                "name":"jane", 
                "userType":"student"},
            "course":{
                "courseID":"COMP1601", 
                "courseName":"Computer Programming I", 
                "type":"Level I", 
                "credits":3, 
                "semester":1, 
                "prerequisite":None, 
                "status":"Unavailable"}
        })
    
    def test_new_courseplan(self):
        student = Student("jane@uwimail.com", "jane", "janepass")
        student.id = 1
        course = Course("COMP1601", "Computer Programming I", "Level I", 3, 1)
        newCoursePlan = CoursePlan(student.id, course.courseID)
        assert newCoursePlan.studentID == 1 and newCoursePlan.courseID == "COMP1601"
    
    def test_courseplanJSON(self):
        student = Student("jane@uwimail.com", "jane", "janepass")
        student.id = 1
        course = Course("COMP1601", "Computer Programming I", "Level I", 3, 1)
        courseplan = CoursePlan(student.id, course.courseID)
        courseplan.student = student
        courseplan.course = course
        courseplan_json = courseplan.toJSON()
        self.assertDictEqual(courseplan_json, {
            "coursePlanID":None,
            "student":{
                "id":1, 
                "email":"jane@uwimail.com", 
                "name":"jane", 
                "userType":"student"},
            "course":{
                "courseID":"COMP1601", 
                "courseName":"Computer Programming I", 
                "type":"Level I", 
                "credits":3, 
                "semester":1, 
                "prerequisite":None, 
                "status":"Unavailable"}
        })


'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()



class UserIntegrationTests(unittest.TestCase):

    @pytest.mark.run(order=1)
    def test_create_staff(self):
        create_staff("rick@uwimail.com", "rick", "rickpass")
        assert get_staff(1) != None

    @pytest.mark.run(order=2)
    def test_create_student(self):
        create_student("rob@uwimail.com", "rob", "robpass")
        assert get_student(1) != None

    @pytest.mark.run(order=3)
    def test_authenticate_staff(self):
        staff = create_staff("bob@uwimail.com", "bob", "bobpass")
        assert login_staff("bob@uwimail.com", "bobpass") != None

    @pytest.mark.run(order=4)
    def test_authenticate_student(self):
        student = create_student("jane@uwimail.com", "jane", "janepass")
        assert login_student("jane@uwimail.com", "janepass") != None

    @pytest.mark.run(order=5)
    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([
            {"id":1, "email":"rick@uwimail.com", "name":"rick", "userType":"staff" },
            {"id":2, "email":"bob@uwimail.com", "name":"bob", "userType":"staff"},
            {"id":1, "email":"rob@uwimail.com", "name":"rob", "userType":"student" },
            {"id":2, "email":"jane@uwimail.com", "name":"jane", "userType":"student" }
            ], users_json)

    @pytest.mark.run(order=6)
    def test_update_staff(self):
        update_staff(2, "bob@uwimail.com", "bobby")
        staff = get_staff(2)
        assert staff.name == "bobby"

    @pytest.mark.run(order=7)
    def test_update_student(self):
        update_student(1, "rob@uwimail.com", "robby")
        student = get_student(1)
        assert student.name == "robby"

    @pytest.mark.run(order=8)
    def test_create_course(self):
        create_course("COMP1601", "Computer Programming I", "Level I", 3, 1)
        assert get_course("COMP1601") != None

    @pytest.mark.run(order=9)
    def test_student_selectPastCourse(self):
        course = get_course("COMP1601")
        student = get_student(2)
        assert student.selectPastCourse(course.courseID) != False
    
    @pytest.mark.run(order=10)
    def test_student_deletePastCourse(self):
        course = get_course("COMP1601")
        student = get_student(2)
        coursehistory = get_coursehistory(student.id, course.courseID)
        assert student.deletePastCourse(coursehistory) != False