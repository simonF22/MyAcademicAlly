from flask_login import login_user, login_manager, logout_user, LoginManager
from flask_jwt_extended import create_access_token, jwt_required, JWTManager

from App.models import User, Staff, Student

def jwt_authenticate(email, password):
    staff = Staff.query.filter_by(email=email).first()
    if staff and staff.check_password(password):
        return create_access_token(identity=email)
    student = Student.query.filter_by(email=email).first()
    if student and student.check_password(password):
        return create_access_token(identity=email)
    return None
    

def login_staff(email, password):
    staff = Staff.query.filter_by(email=email).first()
    if staff and staff.check_password(password):
        return staff
    return None

def login(email, password):    
    student = Student.query.filter_by(email=email).first()
    if student and student.check_password(password):
        return student
    return None

def setup_flask_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        staff = Staff.query.get(user_id)
        if staff:
            return staff
        student = Student.query.get(user_id)
        if student:
            return student
        #return User.query.get(user_id)
    
    return login_manager

def setup_jwt(app):
    jwt = JWTManager(app)

    @jwt.user_identity_loader
    def user_identity_lookup(identity):
        staff = Staff.query.filter_by(email=identity).one_or_none()
        if staff:
            return staff.id
        student = Student.query.filter_by(email=identity).one_or_none()
        if student:
            return student.id
        return None

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        staff = Staff.query.get(identity)
        if staff:
            return staff
        student = Student.query.get(identity)
        if student:
            return student

    return jwt