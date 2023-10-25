from App.database import db
from App.models import User, Staff, Student

def create_user(email, name, password):
    newuser = User(email=email, name=name, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser


def create_staff(email, name, password):
    newuser = Staff(email=email, name=name, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser


def create_student(email, name, password):
    newuser = Student(email=email, name=name, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser


def get_staff(id):
    return Staff.query.get(id)

def get_student(id):
    return Student.query.get(id)

def is_staff(id):
    return Staff.query.get(id) != None

def is_student(id):
    return Student.query.get(id) != None


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    #return User.query.all()
    return Staff.query.all() + Student.query.all()


def get_all_users_json():
    #users = User.query.all()
    staff = Staff.query.all()
    students = Student.query.all()
    users = []
    if not (staff or students):
        return []
    
    for sta in staff:
        users.append(sta.toJSON())
    
    for stu in students:
        users.append(stu.toJSON())
    
    return users

'''
def update_user(id, email):
    user = get_user(id)
    if user:
        user.email = email
        db.session.add(user)
        return db.session.commit()
    return None
'''

def update_staff(id, email, name):
    user = get_staff(id)
    if user:
        user.email = email
        user.name = name
        db.session.add(user)
        return db.session.commit()
    return None

def update_student(id, email, name):
    user = get_student(id)
    if user:
        user.email = email
        user.name = name
        db.session.add(user)
        return db.session.commit()
    return None
    