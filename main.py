from flask import Flask, render_template, request
from flask_restplus import Resource, Api
import flask_admin
from flask_admin.contrib import appengine
from google.appengine.ext import db
from google.appengine.ext import ndb


app = Flask(__name__)
app.config['SECRET_KEY'] = '123456790'
admin = flask_admin.Admin(app, name="Admin")

api = Api(app,doc='/apidoc/',version='1.0')

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello' : 'world'}

@app.route('/main')
def index_page():
    return render_template('index.html')



class Restroom(ndb.Model):
    name = ndb.StringProperty()
    NumOfRooms = ndb.IntegerProperty()
    NumOfVacantRooms = ndb.IntegerProperty()



admin.add_view(appengine.ModelView(Restroom))

