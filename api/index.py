from flask import Flask, request
from flask_restful import Resource, Api
import os
import sys
sys.path.append(os.getcwd()+'\\controller')
print(sys.path)

# print(os.getcwd())

import username
from GMM1 import *

app = Flask(__name__)
api = Api(app)


class Recognition(Resource):
    # def get(self):
    #     return {'hello': 'world'}

    def post(self):
        file = request.files.getlist("file[]")

        file[0].save("training_data/testfile.wav")
        return "Hello: " + username.test1()


class TrainSpeaker(Resource):
    def post(self):
        file = request.files.getlist("file[]")
        nameSpeaker = request.form['name']

        for i in range(5):
            path_store = 'training_data/nguyen_phu_trong' + str(i+1) + '.wav'
            file[i].save(path_store)


        traine(nameSpeaker)

        return nameSpeaker


api.add_resource(Recognition, '/recognize')
api.add_resource(TrainSpeaker, '/train')


if __name__ == '__main__':
    app.run(debug=True)

