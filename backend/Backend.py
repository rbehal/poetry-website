# Using flask to make an api 
# import necessary libraries and functions 
import flask
from flask import Flask, jsonify, request, redirect
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin
import os
import cloudconvert
import zipfile

# PDF Processing #

def downloadImages():
	# Calling api to convert images
	api = cloudconvert.Api('tpdYmzoswVXlDQoU0qz54F7sCs9HOBu06lkDV3BJz8oyUhGBpgbDQD3Fw0goOhKH')
	process = api.convert({
		"inputformat": "pdf",
		"outputformat": "png",
		"input": "upload",
		"file": open('poems.pdf', 'rb')
	})
	process.wait()
	# Downloading images to raw_images folder
	process.download("raw_images/")

def createRawImages():
	# Extracting zip file
	with zipfile.ZipFile("raw_images/poems.zip", 'r') as zip_ref:
		zip_ref.extractall("raw_images/")

	# Deleting zip file
	os.remove("raw_images/poems.zip")
	os.remove("poems.pdf")

	# Renaming images
	for filename in os.listdir("raw_images/"):
		if filename.endswith(".png"):
			image_path = "raw_images/"
			if (filename[-7:-4].isdigit()):
				os.rename(image_path + filename, image_path + filename[-7:-4] + ".png")
			elif (filename[-6:-4].isdigit()):
				os.rename(image_path + filename, image_path + filename[-6:-4] + ".png")
			elif (filename[-5].isdigit()):
				os.rename(image_path + filename, image_path + filename[-5] + ".png")    
		else:
			continue


# Creating a Flask app #

app = Flask(__name__) 

@app.route("/", methods = ['GET']) 
def home_view():
	return "<h1>Poem website backend is deployed :)</h1>"

@app.route("/upload", methods = ['GET','POST']) 
def upload_image():
	if request.method == "POST":
		if request.files:
			poems = request.files["poems"]
			poems.save(os.getcwd() + "/poems.pdf")
			downloadImages()
			createRawImages()
			return redirect(request.referrer)
	return 'NOT OK'

# Driver function - must be at the end
if __name__ == '__main__': 
	app.run()