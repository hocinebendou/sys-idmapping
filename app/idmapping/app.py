from flask import Flask
from flask_restful import Resource, Api, fields, marshal, reqparse
from flask_httpauth import HTTPBasicAuth

from resources.generateId import GenerateID
from resources.generateId import IdMappingInfo

print ("APP STARTED")

app = Flask(__name__)

api =   Api(app)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'userapi':
        return 'changepassword'
    return None

@app.route('/')
def home():
    return "ID MAPPING / DEVELOPMENT VERSION 0.1"

'''
@app.errorhandler(Exception)
def all_exception_handler(error):
   return 'Some Python Error appeared', 500
'''

@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)


api.add_resource(GenerateID, '/idmapping/api/v1.0/generate',      endpoint='generate')
api.add_resource(IdMappingInfo, '/idmapping/api/v1.0/info/<string:fullid>', endpoint='info')

if __name__ == '__main__':
    app.run(debug=True)
