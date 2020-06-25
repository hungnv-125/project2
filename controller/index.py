from flask import Flask, request
from flask_restful import Resource, Api
from controller.username import *

app = Flask(__name__)
api = Api(app)

class Upload(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        file = request.files.getlist("file[]")

        file[0].save("testfile.wav")
        return "Hello: " + test1()

api.add_resource(Upload, '/')

if __name__ == '__main__':
    app.run(debug=True)

