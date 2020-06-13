# Using flask to make an api 
# import necessary libraries and functions 
import flask
from flask import Flask, jsonify, request, redirect
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin
import os

# creating a Flask app 
app = Flask(__name__) 


@app.route("/", methods = ['GET']) 
def home_view():
	return "<h1>Poem website backend is deployed :)</h1>"

@app.route("/upload", methods = ['GET','POST']) 
def upload_image():
	if request.method == "POST":
		if request.files:
			poems = request.files["poems"]
			print(poems)
			print(os.getcwd())
			poems.save(os.getcwd() + "/poems.pdf")
			return redirect(request.referrer)
	return 'NOT OK'

# driver function - must be at the end
if __name__ == '__main__': 
	app.run()