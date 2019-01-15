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

class House(ndb.Model):
    address = db.StringProperty()
    json_property = ndb.JsonProperty()
    indexed_int = ndb.IntegerProperty()
    unindexed_int = ndb.IntegerProperty(indexed=False)
    text_property = ndb.TextProperty()

class Room(ndb.Model):
    house = ndb.KeyProperty(kind=House)
    name = ndb.StringProperty()

admin.add_view(appengine.ModelView(House))
admin.add_view(appengine.ModelView(Room))
