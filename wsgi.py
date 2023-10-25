import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.main import create_app
from App.controllers import (
    create_user, create_staff, create_student, get_all_users_json, get_all_users, 
    create_course, get_course, get_all_courses, get_all_courses_json,
    create_programme, get_programme, get_all_programmes, get_all_programmes_json, 
    create_course_programme, get_all_course_programme, get_all_course_programme_json )

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    db.drop_all()
    db.create_all()
    create_staff('bob@uwimail.com', 'bob', 'bobpass')
    create_student('jane@uwimail.com', 'jane', 'janepass')
    
    create_programme('CS_Spec', 'BSc Computer Science (Special)', 'FST', 24, 60, 9, 93, 'Level One: 24 Core Credits | Advanced Level: 60 Credits (45 Core Credits + 15 Elective Credits) | Foundation: 9 Credits')
    #create_programme('CS_Major', 'Major in Computer Science', 'FST', 24, 60, 9, 93, 'Level One: 12 CompSci Core Credits | Advanced Level: 30 CompSci Credits (18 Core Credits + 12 Elective Credits) | Foundation: 9 Credits')
    #create_programme('CS_Minor', 'Minor in Computer Science', 'FST', 24, 60, 9, 93, 'Level One: 12 CompSci Core Credits | Advanced Level: 15 CompSci Credits (9 Core Credits + 6 Elective Credits) | Foundation: 9 Credits')

    create_course('COMP1600', 'Introduction to Computing Concepts', 'Level One', 3, 1)
    create_course('COMP1601', 'Computer Programming I', 'Level One', 3, 1)
    create_course('COMP2601', 'Computer Architecture', 'Advanced Level', 3, 1, 'COMP1600')
    create_course('COMP2602', 'Computer Networks', 'Advanced Level', 3, 1, 'COMP1600')
    create_course('COMP2605', 'Enterprise Database Systems', 'Advanced Level', 3, 1, 'COMP1602')
    create_course('COMP2611', 'Data Structures', 'Advanced Level', 3, 1, 'COMP1602')
    create_course('COMP3602', 'Theory of Computing', 'Advanced Level', 3, 1, 'COMP1604')
    create_course('COMP3603', 'Human Computer Interaction', 'Advanced Level', 3, 1, 'COMP2606')
    create_course('COMP3605', 'Introduction to Data Analytics', 'Advanced Level', 3, 1, 'MATH2250')
    create_course('COMP3606', 'Wireless and Mobile Computing', 'Advanced Level', 3, 1, 'COMP2602')
    create_course('COMP3607', 'Object-Oriented Programming II', 'Advanced Level', 3, 1, 'COMP2603')
    create_course('COMP3613', 'Software Engineering II', 'Advanced Level', 3, 1, 'COMP2606')

    create_course('COMP1602', 'Computer Programming II', 'Level One', 3, 2)
    create_course('COMP1603', 'Computer Programming III', 'Level One', 3, 2)
    create_course('COMP1604', 'Mathematics for Computing', 'Level One', 3, 2)
    create_course('COMP2603', 'Object-Oriented Programming I', 'Advanced Level', 3, 2, 'COMP1603')
    create_course('COMP2604', 'Operating Systems', 'Advanced Level', 3, 2, 'COMP1600')
    create_course('COMP2606', 'Software Engineering I', 'Advanced Level', 3, 2, 'COMP1602')
    create_course('COMP3601', 'Design and Analysis of Algorithms', 'Advanced Level', 3, 2, 'COMP2611')
    create_course('COMP3608', 'Intelligent Systmes', 'Advanced Level', 3, 2, 'COMP2611')
    create_course('COMP3609', 'Game Programming', 'Advanced Level', 3, 2, 'COMP2603')
    create_course('COMP3610', 'Big Data Analytics', 'Advanced Level', 3, 2, 'COMP3605')
    create_course('COMP3611', 'Modelling and Simulation', 'Advanced Level', 3, 2, 'MATH2250')
   
    create_course('INFO1600', 'Introduction to Information Technology Concepts', 'Level One', 3, 1)
    create_course('INFO2605', 'Professional Ethics and Law', 'Advanced Level', 3, 1, 'COMP1600')
    create_course('INFO3600', 'Business Information Systems', 'Advanced Level', 3, 1, 'COMP2605')
    create_course('INFO3605', 'Fundamentals of LAN Technologies', 'Advanced Level', 3, 1, 'COMP2604')

    create_course('INFO1601', 'Introduction to WWW Programming', 'Level One', 3, 2)
    create_course('INFO2602', 'Web Programming and Technologies I', 'Advanced Level', 3, 2, 'INFO1601')
    create_course('INFO2604', 'Information Systems Security', 'Advanced Level', 3, 2, 'COMP1602')
    create_course('INFO3604', 'Project', 'Advanced Level', 3, 2, 'COMP2606')
    create_course('INFO3606', 'Cloud Computing', 'Advanced Level', 3, 2, 'COMP2605')
    create_course('INFO3607', 'Fundamentals of WAN Technologies', 'Advanced Level', 3, 2, 'COMP2604')
    create_course('INFO3608', 'E-Commerce', 'Advanced Level', 3, 2, 'COMP2606')
    create_course('INFO3611', 'Database Administration', 'Advanced Level', 3, 2, 'COMP2605')

    create_course('MATH1115', 'Fundamental Mathematics for General Sciences I', 'Level One', 3, 1)
    create_course('MATH2250', 'Industrial Statistics', 'Advanced Level', 3, 1)

    create_course('FOUN1101', 'Caribbean Civilisation', 'Foundation', 3, 1)
    create_course('FOUN1105', 'Scientific and Technical Writing', 'Foundation', 3, 2)
    create_course('FOUN1301', 'Law, Governance, Economy and Society', 'Foundation', 3, 2)

    create_course_programme('COMP1600', 'CS_Spec')
    create_course_programme('COMP1601', 'CS_Spec')
    create_course_programme('INFO1600', 'CS_Spec')
    create_course_programme('MATH1115', 'CS_Spec')
    create_course_programme('COMP1602', 'CS_Spec')
    create_course_programme('COMP1603', 'CS_Spec')
    create_course_programme('COMP1604', 'CS_Spec')
    create_course_programme('INFO1601', 'CS_Spec')

    create_course_programme('COMP2601', 'CS_Spec')
    create_course_programme('COMP2602', 'CS_Spec')
    create_course_programme('COMP2605', 'CS_Spec')
    create_course_programme('COMP2611', 'CS_Spec')
    create_course_programme('MATH2250', 'CS_Spec')
    create_course_programme('COMP2603', 'CS_Spec')
    create_course_programme('COMP2604', 'CS_Spec')
    create_course_programme('COMP2606', 'CS_Spec')
    create_course_programme('INFO2602', 'CS_Spec')
    create_course_programme('INFO2604', 'CS_Spec')

    create_course_programme('COMP3602', 'CS_Spec')
    create_course_programme('COMP3603', 'CS_Spec')
    create_course_programme('COMP3613', 'CS_Spec')
    create_course_programme('COMP3601', 'CS_Spec')
    create_course_programme('INFO3604', 'CS_Spec')

    create_course_programme('COMP3605', 'CS_Spec')
    create_course_programme('COMP3607', 'CS_Spec')
    create_course_programme('INFO2605', 'CS_Spec')
    create_course_programme('INFO3600', 'CS_Spec')
    create_course_programme('INFO3605', 'CS_Spec')

    create_course_programme('COMP3608', 'CS_Spec')
    create_course_programme('COMP3609', 'CS_Spec')
    create_course_programme('COMP3610', 'CS_Spec')
    create_course_programme('COMP3611', 'CS_Spec')
    create_course_programme('INFO3606', 'CS_Spec')
    create_course_programme('INFO3607', 'CS_Spec')
    create_course_programme('INFO3608', 'CS_Spec')
    create_course_programme('INFO3611', 'CS_Spec')

    create_course_programme('FOUN1101', 'CS_Spec')
    create_course_programme('FOUN1105', 'CS_Spec')
    create_course_programme('FOUN1301', 'CS_Spec')
    

    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup("user", help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create-staff", help="Creates a staff user")
@click.argument("email", default="rob@uwimail.com")
@click.argument("name", default="rob")
@click.argument("password", default="robpass")
def create_staff_command(email, name, password):
    create_staff(email, name, password)
    print(f'{email} created!')

@user_cli.command("create-student", help="Creates a student user")
@click.argument("email", default="rachel@uwimail.com")
@click.argument("name", default="rachel")
@click.argument("password", default="rachelpass")
def create_student_command(email, name, password):
    create_student(email, name, password)
    print(f'{email} created!')

# this command will be : flask user create staff rob@uwimail.com rob robpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())
    
@user_cli.command("courses", help="Lists courses in the database")
@click.argument("format", default="string")
def list_courses_command(format):
    if format == 'string':
        print(get_all_courses())
    else:
        print(get_all_courses_json())

@user_cli.command("programmes", help="Lists programmes in the database")
@click.argument("format", default="string")
def list_programmes_command(format):
    if format == 'string':
        print(get_all_programmes())
    else:
        print(get_all_programmes_json())



app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)