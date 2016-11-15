import json
from flask import Flask, jsonify
from flask_restful import Resource, Api, fields, marshal, reqparse, request


class GenerateID(Resource):
#    decorators = [auth.login_required]

    def __init__(self):
        super(GenerateID, self).__init__()

    def get(self):


        print request.url
        return "123", 200


