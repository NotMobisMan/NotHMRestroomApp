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
"""

"""
@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello' : Restroom.get_list().fetch()}

@app.route('/main')
def index_page():
    restrooms = Restroom.get_list().fetch();
    return render_template('index.html',restrooms = restrooms)

# API for Decreasing the number of vacant rooms
@api.route('/Down/<string:url>')
class Down(Resource):
    def get(self,url):
        targetKey = ndb.Key(urlsafe=url)
        target = targetKey.get()
        
        NumOfVacantRooms = target.NumOfVacantRooms
        Before = NumOfVacantRooms

        if NumOfVacantRooms > 0 :
            NumOfVacantRooms = NumOfVacantRooms - 1
        target.NumOfVacantRooms = NumOfVacantRooms
        target.put()
        After = NumOfVacantRooms

        return {'status' : 'ok', 'before':Before, 'after' : After}




# API for increasing the number of vacant rooms
@api.route('/Up/<string:url>')
class Up(Resource):
    def get(self,url):
        targetKey = ndb.Key(urlsafe=url)
        target = targetKey.get()
        
        NumOfVacantRooms = target.NumOfVacantRooms
        Before = NumOfVacantRooms

        if NumOfVacantRooms < target.NumOfRooms :
            NumOfVacantRooms = NumOfVacantRooms + 1

        target.NumOfVacantRooms = NumOfVacantRooms
        target.put()
        After = NumOfVacantRooms

        return {'status' : 'ok', 'before':Before, 'after' : After}


class Restroom(ndb.Model):
    name = ndb.StringProperty()
    NumOfRooms = ndb.IntegerProperty()
    NumOfVacantRooms = ndb.IntegerProperty()

    @classmethod
    def get_list(cls):
        return cls.query()



admin.add_view(appengine.ModelView(Restroom))

