from flask import Flask
from flask_restful import Resource, Api

application = Flask(__name__)
api = Api(application)

@application.route('/')
def index():
    return "Hello World!"

class HealthCheck(Resource):
    def get(self):
        return 'OK'

api.add_resource(HealthCheck, '/ws/healthz/')
