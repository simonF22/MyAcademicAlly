import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import User, Staff, Student, Course
from App.controllers import (
    create_staff, create_student, get_all_users_json,
    login_staff, login_student,
    
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
        self.assertDictEqual(staff_json, {"id":None, "email":"bob@uwimail.com", "name":"bob", "userType":"staff"})

    def test_studentJSON(self):
        student = Student("jane@uwimail.com", "jane", "janepass")
        student_json = student.toJSON()
        self.assertDictEqual(student_json, {"id":None, "email":"jane@uwimail.com", "name":"jane", "userType":"student"})

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
        newcourse = Course('COMP1601', 'Computer Programming I', 'Level One', 3, 1)
        assert newcourse.courseID == "COMP1601"
    
    def test_courseJSON(self):
        course = Course('COMP1601', 'Computer Programming I', 'Level One', 3, 1)
        course_json = course.toJSON()
        self.assertDictEqual(course_json, {
        "courseID":"COMP1601", 
        "courseName":"Computer Programming I", 
        "type":"Level One", 
        "credits":3,
        "semester":1,
        "prerequisite":None,
        "status":"Unavailable"
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


def test_authenticate():
    user = create_user("bob", "bobpass")
    assert login("bob", "bobpass") != None

class UsersIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("rick", "bobpass")
        assert user.username == "rick"

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([{"id":1, "username":"bob"}, {"id":2, "username":"rick"}], users_json)

    # Tests data changes in the database
    def test_update_user(self):
        update_user(1, "ronnie")
        user = get_user(1)
        assert user.username == "ronnie"
