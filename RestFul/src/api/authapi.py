from src.model.User import User
from flask_restful import Resource
from flask import Response, request
from flask_jwt_extended import create_access_token
import datetime

def check_email(email):
    if User.objects(email=email).first():
        return True
    return False
  
def check_username(username):
    if User.objects(username=username).first():
        return True
    return False


class SignupApi(Resource):
    ''' 
    endpoint : /api/signup
    Request method : POST
    '''
    def post(self):
        body = request.get_json()
        email = body["email"]
        username = body["username"]
        # check if email already exists
        if check_email(email):
            return Response(response="Email already exists", status=400)
        user = User(**body)
        # check if username already exists
        if check_username(username):
            return Response(response="Username already exists", status=400)

        # if body has password 
        if body.get('password'):
            user.hash_password()
        if 'image' in request.files:
            image = request.files['image']
        user.save_image(request.files['image'])
        user.save()
        expires = datetime.timedelta(days=7)
        
        access_token = create_access_token(identity=str(user.username), expires_delta=expires)
        return {'token': access_token}, 200

class LoginApi(Resource):
    ''' 
    endpoint : /api/login
    Request method : POST
    '''

    def post(self):
        body = request.get_json()
        try:
            user = User.objects.get(username=body['username'])
            authorized = user.check_password(body.get('password'))

        except User.DoesNotExist:
            return {'message': 'User does not exist'}, 404

        if not authorized:
            return {'error': 'Email or password invalid'}, 401

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.username), expires_delta=expires)
        return {'token': access_token}, 200
    