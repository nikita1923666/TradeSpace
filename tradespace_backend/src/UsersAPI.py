from flask import Blueprint, jsonify, request
from TokenAuthentication import auth
import firebase_admin
from firebase_admin import auth as firebase_auth
from firebase_admin import _auth_utils as firebase_auth_utils
users_api = Blueprint('users_api', __name__)

@users_api.route('/')
def hello():
  return 'Users: Hello World!'

@users_api.route('/<string:user_id>', methods=['GET'])
@auth.login_required
def get_user_with_id(user_id):
  try:
    user = firebase_auth.get_user(user_id)
    user_data = jsonify(display_name=user.display_name, email=user.email, phone_number=user.phone_number)
    return user_data
  except firebase_auth_utils.UserNotFoundError:
    return {'error': 'user id not found'}, 400

@users_api.route('/', methods=['POST'])
def create_user():
  try:
    email = request.form['email']
    password = request.form['password']
    display_name = request.form['display_name']
    phone_number = request.form['phone_number']
    user = firebase_auth.create_user(email=email, password=password, display_name=display_name, phone_number=phone_number)
    return "User Created", 201
  except firebase_auth_utils.EmailAlreadyExistsError:
    return {'error': 'email already exists'}, 400
  except firebase_auth_utils.PhoneNumberAlreadyExistsError:
    return {'error': 'phone number already exists'}, 400
  except firebase_auth_utils.UnexpectedResponseError:
    return {'error': 'unexpected response'}, 400
  except:
    return {'error': 'request error'}, 400
