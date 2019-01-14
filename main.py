from flask import Flask, render_template, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app,doc='/apidoc/',version='1.0')

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello' : 'world'}

