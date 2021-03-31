import flask
import requests
import base64
from flask import Flask, Response,redirect,render_template,request
# from flask_restful import reqparse, abort,url_for,Resource,Api
from flask_restplus import Resource, Api, apidoc
app = Flask(__name__)
api = Api(app, version='1.0', title='restful API',
    description='A simple API',doc="/apis/docs/",prefix="/apis"
)
from flask import request, jsonify

class Infer(Resource):

    def get(self,id=None):
        print(request.data,request.headers)
        if id:
            print(id)
        print(222)



api.add_resource(Infer, '/Infer','/Infer/<id>')

if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0",threaded=True)