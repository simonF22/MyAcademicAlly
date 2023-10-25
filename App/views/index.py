from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import create_user

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_staff('bob@uwimail.com', 'bob', 'bobpass')
    create_student('jane@uwimail.com', 'jane', 'janepass')
    
    ''' PROGRAMME CREATION '''
    create_programme('CS_Spec', 'BSc Computer Science (Special)', 'FST', 24, 60, 9, 93, 'Level One: 24 Core Credits | Advanced Level: 60 Credits (45 Core Credits + 15 Elective Credits) | Foundation: 9 Credits')
    
    ''' COURSE CREATION '''
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


    ''' COURSE-PROGRAMME CREATION '''
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
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})