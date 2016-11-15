import json
from flask import Flask, jsonify
from flask_restful import Resource, Api, fields, marshal, reqparse, request
import requests
import execjs

class IdMappingInfo(Resource):
#    decorators = [auth.login_required]

    def __init__(self):
        super(IdMappingInfo, self).__init__()

    def get(self, id):

        print (request.url)

        instanceName = id.split('.')[0]
        applicationID = id.split('::')[0]
        localID = id.split('::')[1]

        print("id =", id)
        print("applicationID =", applicationID)
        print("localID =", localID)

        print(instanceName)
        url = "http://development.bibbox.org/api/jsonws/BIBBOXDocker-portlet.get-id-mapping-info?instanceId="+instanceName
        print(url)

        r = requests.get(url,  auth=('userapi', 'changepassword'))
        idmaping_info = json.loads (r.text)
        javascriptCodeArray = idmaping_info['mappings']['SUBJECT']['human_readable']

        js = ''
        for l in javascriptCodeArray:
            l = l.replace ("&&aid", applicationID)
            l = l.replace ("&&id1", localID)
            print (l)
            js = js + l

        r = execjs.eval(js)
        print (r)

        idmaping_info['resolved-mappings'] = {}
        idmaping_info['resolved-mappings']['id'] = id
        idmaping_info['resolved-mappings']['mappings'] = {}
        idmaping_info['resolved-mappings']['mappings']['human-readable'] = r

        javascriptCodeArray = idmaping_info['mappings']['SUBJECT']['get_info']

        js = ''
        for l in javascriptCodeArray:
            l = l.replace ("&&aid", applicationID)
            l = l.replace ("&&id1", localID)
            print (l)
            js = js + l

        r = execjs.eval(js)
        print (r)
        idmaping_info['resolved-mappings']['mappings']['url'] = r

        return idmaping_info, 200

'''
http://development.bibbox.org/api/jsonws/BIBBOXDocker-portlet.get-id-mapping-info?instanceId=pt99
http://127.0.0.1:5000/idmapping/api/v1.0/info/pt99.development.bibbox.org::P0000002
'''

class GenerateID(Resource):
#    decorators = [auth.login_required]

    def __init__(self):
        super(GenerateID, self).__init__()

    def get(self):

        print (request.url)
        return "123", 200


