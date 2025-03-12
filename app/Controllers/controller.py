#This is the main controller file, contains all the routes and endpoints.
#All the API request are received in this file.

from flask import Blueprint, jsonify, request
from app.Services.CalorieInformation import get_CalorieInfo
from app.Services.Calories import get_nutrition_info
from  app.Services.UserAcess import user_registration
from app.Services.UserAcess import user_login
from app.Services.CustomInformation import get_custom_info
from app.Services.CalorieGoal import get_calorie_goal
from flask_jwt_extended import jwt_required

import config as config
controller_bp = Blueprint('controller', __name__)


#This is just a dummy service for testing purpose.
@controller_bp.route('/calories', methods=['GET'])
def get_calorie_info():
    calorie_info = get_CalorieInfo()
    return jsonify(calorie_info), 200

#This service provides output of the nutrients like protien,carbs,fat,fiber, and vitamins
@controller_bp.route('/get_nutrition', methods=['GET', 'POST'])
@jwt_required()
def get_nutrition():
    
    if request.method == 'GET':
        return jsonify({"message": "Use a POST request with a food item in JSON format."}), 405
 
    data = request.json
 
    food_item = data.get("food")
    weight = data.get("weight")
    if not food_item:
        return jsonify({"error": "Please provide a food item"}), 400

    nutrition_info = get_nutrition_info(food_item,weight)
    return jsonify(nutrition_info)


#This service provides output for the field other questions from frontend.
@controller_bp.route('/get_custom',methods = ['GET','POST'])
@jwt_required()
def get_custom():
    data = request.json
    food_item = data.get("food")
    weight = data.get("weight")
    custom = data.get("custom")
    if not food_item:
        return jsonify({"error": "Please provide a food item"}), 400
    if not custom:
        return jsonify({"error": "Please provide a food item"}), 400
    custom_info = get_custom_info(food_item,weight,custom)
    return jsonify(custom_info)


#Responsible for registration
@controller_bp.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    userCreation = user_registration(email,password)

    return userCreation

#Responsible for login
@controller_bp.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    userAccess = user_login(email,password)
    return userAccess


#This service provides output about for the calori Guide page, where user can input their weight and age. Responsible for providing calories required per day.
@controller_bp.route('/get_calorieGoal',methods = ['GET','POST'])
@jwt_required()
def get_calorieGoal():
    data = request.json
    weight = data.get("weight")
    age = data.get("age")
    

    if not weight:
        return jsonify({"error": "Please provide a food item"}), 400
    if not age:
        return jsonify({"error": "Please provide a food item"}), 400
   
    calorie = get_calorie_goal(weight,age)
    return jsonify(calorie)
