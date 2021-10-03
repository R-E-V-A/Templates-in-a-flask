from  src.api.authapi import SignupApi, LoginApi

def initialize_routes(api):
    api.add_resource(SignupApi, '/api/signup')
    api.add_resource(LoginApi, '/api/login')
