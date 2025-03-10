from flask import Blueprint, jsonify, request
from app.Services.CalorieInformation import get_CalorieInfo
from app.Services.Calories import get_nutrition_info
from  app.Services.UserAcess import user_registration
from app.Services.UserAcess import user_login
from app.Services.CustomInformation import get_custom_info

import config as config
controller_bp = Blueprint('controller', __name__)

@controller_bp.route('/calories', methods=['GET'])
def get_calorie_info():
    calorie_info = get_CalorieInfo()
    return jsonify(calorie_info), 200

@controller_bp.route('/get_nutrition', methods=['GET', 'POST'])
def get_nutrition():
    
    """API endpoint to fetch nutrition data."""
    if request.method == 'GET':
        return jsonify({"message": "Use a POST request with a food item in JSON format."}), 405
 
    data = request.json
 
    food_item = data.get("food")
    weight = data.get("weight")
    if not food_item:
        return jsonify({"error": "Please provide a food item"}), 400

    nutrition_info = get_nutrition_info(food_item,weight)
    # print(json.dumps(nutrition_info, indent=2))
    return jsonify(nutrition_info)


@controller_bp.route('/get_custom',methods = ['GET','POST'])
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



@controller_bp.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    userCreation = user_registration(email,password)

    return userCreation

@controller_bp.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    userAccess = user_login(email,password)
    return userAccess