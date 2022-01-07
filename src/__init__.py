from flask import Flask, jsonify
from flask_restx import Resource, api


# instatiate the app
app = Flask(__name__)

api = Api(app)


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(Ping, '/ping')