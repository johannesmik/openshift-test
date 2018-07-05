from flask import Flask, request
from flask_restful import Resource, Api
from marshmallow import Schema, fields, post_load

class Text(object):
    def __init__(self, text):
        self.text = text

class TextSchema(Schema):
    text = fields.String()

    @post_load
    def make_text(self, data):
        assert 'text' in data, "Must specify text in request"
        return Text(text=data['text'])

class HealthCheck(Resource):
    def get(self):
        return 'OK'

api.add_resource(HealthCheck, '/ws/healthz/')

application = Flask(__name__)
api = Api(application)

@application.route('/')
def index():
    return "Hello World!"

@application.route('/textlength', methods=['POST'])
def textlength():
    text = TextSchema().load(request.get_json()).data
    
    return {'success': True, 'textlength': len(text.text) }

