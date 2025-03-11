from app import create_app
from flask_cors import CORS
from flask_jwt_extended import JWTManager



app = create_app()
CORS(app)

app.config['JWT_SECRET_KEY'] = 'konvi'  
jwt = JWTManager(app)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

