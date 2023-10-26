from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db

from App.controllers import (
    create_staff, create_student,
    create_programme, create_course, create_course_programme
)

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    try:
        db.drop_all()
        db.create_all()
        create_staff('bob@uwimail.com', 'bob', 'bobpass')
        create_student('jane@uwimail.com', 'jane', 'janepass')

        ''' PROGRAMME CREATION '''
        create_programme('CS_Spec', 'BSc Computer Science (Special)', 'FST', 24, 60, 9, 93, 'Level One: 24 Core Credits | Advanced Level: 60 Credits (45 Core Credits + 15 Elective Credits) | Foundation: 9 Credits')

        ''' COURSE CREATION '''
        create_course('MATH1115', 'Fundamental Mathematics for General Sciences I', 'Level I', 3, 1)
        create_course('MATH2250', 'Industrial Statistics', 'Level II', 3, 1)

        create_course('FOUN1101', 'Caribbean Civilisation', 'Foundation', 3, 1)
        create_course('FOUN1105', 'Scientific and Technical Writing', 'Foundation', 3, 2)
        create_course('FOUN1301', 'Law, Governance, Economy and Society', 'Foundation', 3, 2)

        create_course('COMP1600', 'Introduction to Computing Concepts', 'Level I', 3, 1)
        create_course('COMP1601', 'Computer Programming I', 'Level I', 3, 1)
        create_course('COMP1602', 'Computer Programming II', 'Level I', 3, 2)
        create_course('COMP1603', 'Computer Programming III', 'Level I', 3, 2)
        create_course('COMP1604', 'Mathematics for Computing', 'Level I', 3, 2)
        create_course('INFO1600', 'Introduction to Information Technology Concepts', 'Level I', 3, 1)
        create_course('INFO1601', 'Introduction to WWW Programming', 'Level I', 3, 2)
        
        create_course('COMP2601', 'Computer Architecture', 'Level II', 3, 1, 'COMP1600')
        create_course('COMP2602', 'Computer Networks', 'Level II', 3, 1, 'COMP1600')
        create_course('COMP2603', 'Object-Oriented Programming I', 'Level II', 3, 2, 'COMP1603')
        create_course('COMP2604', 'Operating Systems', 'Level II', 3, 2, 'COMP1600')
        create_course('COMP2605', 'Enterprise Database Systems', 'Level II', 3, 1, 'COMP1602')
        create_course('COMP2606', 'Software Engineering I', 'Level II', 3, 2, 'COMP1602')
        create_course('COMP2611', 'Data Structures', 'Level II', 3, 1, 'COMP1602')
        create_course('INFO2602', 'Web Programming and Technologies I', 'Level II', 3, 2, 'INFO1601')
        create_course('INFO2604', 'Information Systems Security', 'Level II', 3, 2, 'COMP1602')
        create_course('INFO2605', 'Professional Ethics and Law', 'Level II', 3, 1, 'COMP1600')

        create_course('COMP3601', 'Design and Analysis of Algorithms', 'Level III', 3, 2, 'COMP2611')
        create_course('COMP3602', 'Theory of Computing', 'Level III', 3, 1, 'COMP1604')
        create_course('COMP3603', 'Human Computer Interaction', 'Level III', 3, 1, 'COMP2606')
        create_course('COMP3605', 'Introduction to Data Analytics', 'Level III', 3, 1, 'MATH2250')
        create_course('COMP3606', 'Wireless and Mobile Computing', 'Level III', 3, 1, 'COMP2602')
        create_course('COMP3607', 'Object-Oriented Programming II', 'Level III', 3, 1, 'COMP2603')
        create_course('COMP3608', 'Intelligent Systmes', 'Level III', 3, 2, 'COMP2611')
        create_course('COMP3609', 'Game Programming', 'Level III', 3, 2, 'COMP2603')
        create_course('COMP3610', 'Big Data Analytics', 'Level III', 3, 2, 'COMP3605')
        create_course('COMP3611', 'Modelling and Simulation', 'Level III', 3, 2, 'MATH2250')
        create_course('COMP3613', 'Software Engineering II', 'Level III', 3, 1, 'COMP2606')
        create_course('INFO3600', 'Business Information Systems', 'Level III', 3, 1, 'COMP2605')
        create_course('INFO3605', 'Fundamentals of LAN Technologies', 'Level III', 3, 1, 'COMP2604')
        create_course('INFO3604', 'Project', 'Level III', 3, 2, 'COMP2606')
        create_course('INFO3606', 'Cloud Computing', 'Level III', 3, 2, 'COMP2605')
        create_course('INFO3607', 'Fundamentals of WAN Technologies', 'Level III', 3, 2, 'COMP2604')
        create_course('INFO3608', 'E-Commerce', 'Level III', 3, 2, 'COMP2606')
        create_course('INFO3611', 'Database Administration', 'Level III', 3, 2, 'COMP2605')

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
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error initializing application: {str(e)}'})

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})