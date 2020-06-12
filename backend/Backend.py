# Using flask to make an api 
# import necessary libraries and functions 
import flask
import requests
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin

# creating a Flask app 
app = Flask(__name__) 


@app.route("/", methods = ['GET']) 
def home_view(): 
        return "<h1>Poem website backend is deployed :)</h1>"


# driver function - must be at the end
if __name__ == '__main__': 
    app.run() 
