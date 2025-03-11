#This service receives response from userAcess service.
#This service receives requests from user_regisration and user_login service.
#Also responsible for generating hash password and checking hash password.

from app.Models.users import User
from werkzeug.security import generate_password_hash, check_password_hash

users = []
def add_user(userName, password):
    hashed_password = generate_password_hash(password)
    user = User(userName,hashed_password)
    users.append(user)

def check_userName(userName):
    for user in users:
        if user.get_userName() == userName:
            return True
    return False
    
def check_user(userName, password):
    for user in users:
        if user.get_userName() == userName and check_password_hash(user.get_password(), password):
            return True
    return False