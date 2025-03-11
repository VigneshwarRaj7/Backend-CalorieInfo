#This service provides response for Login and authenticaion. 
#It also connect with userManagement service.

from flask import Flask, request, jsonify
import json
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from app.Services.userManagement import check_userName,check_user,add_user

from app.Models.users import User



def user_registration(email,password):
    if not email or not password:
        return jsonify({'error': 'Email and password are required.'}), 400

    if check_userName(email):
        return jsonify({'error': 'User already exists.'}), 400

    
    add_user(email,password)
    return jsonify({'message': 'User registered successfully.'}), 200


def user_login(email,password):
    if not email or not password:
        return jsonify({'error': 'Email and password are required.'}), 400

    
    if check_userName(email):
        if not check_user(email,password):
            return jsonify({'error': 'Invalid credentials.'}), 401
    else:
        return jsonify({'error': 'User not found.'}), 404

    access_token = create_access_token(identity=email)
    
    return jsonify({'token': access_token}), 200
