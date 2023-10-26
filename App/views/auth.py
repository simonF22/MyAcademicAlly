from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user

from.index import index_views

from App.controllers import (
    get_all_users, get_all_users_json,
    create_staff, create_student,
    jwt_authenticate,
    login_staff, login_student 
)

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')

'''
Page/Action Routes
'''

@auth_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)


@auth_views.route('/identify', methods=['GET'])
@login_required
def identify_page():
    return jsonify({'message': f"id : {jwt_current_user.id}"})


@auth_views.route('/login', methods=['POST'])
def login_action():
    data = request.json
    user = login(data['email'], data['password'])
    if user:
        if login(data['email'], data['password']):
            return jsonify({"message":"user logged in!"})
    return 'bad email or password given', 401

@auth_views.route('/logout', methods=['GET'])
def logout_action():
    data = request.json
    user = login(data['email'], data['password'])
    return 'logged out!'

'''
API Routes
'''

@auth_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@auth_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    create_user(data['email'], data['name'], data['password'], data['userType'])
    return jsonify({'message': f"user {data['email']} created"})

@auth_views.route('/api/login', methods=['POST'])
def user_login_api():
  data = request.json
  email = data['email']
  password = data['password']
  token = jwt_authenticate(email, password)
  if token:
    return jsonify(access_token=token)
  return jsonify(error='bad email or password given'), 401

@auth_views.route('/api/identify', methods=['GET'])
@jwt_required()
def identify_user_action():
    return jsonify({'message': f"id : {jwt_current_user.id}"})