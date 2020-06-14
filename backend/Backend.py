# Using flask to make an api 
# import necessary libraries and functions 
import flask
from flask import Flask, jsonify, request, redirect
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin

import os
import cloudconvert
import zipfile

import cloudinary.uploader
import cloudinary.api
import json

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
	images_path = "raw_images/"

	# Extracting zip file
	with zipfile.ZipFile(images_path + "poems.zip", 'r') as zip_ref:
		zip_ref.extractall(images_path)

	# Deleting zip file
	os.remove(images_path + "poems.zip")
	os.remove("poems.pdf")

	# Renaming images
	num_pages = 0
	for filename in os.listdir(images_path):
		if filename.endswith(".png"):
			if (filename[-7:-4].isdigit()):
				os.rename(images_path + filename, images_path + filename[-7:-4] + ".png")
				num_pages += 1
			elif (filename[-6:-4].isdigit()):
				os.rename(images_path + filename, images_path + filename[-6:-4] + ".png")
				num_pages += 1
			elif (filename[-5].isdigit()):
				os.rename(images_path + filename, images_path + filename[-5] + ".png")    
				num_pages += 1
		else:
			continue
	uploadImages(num_pages)

def uploadImages(num_pages):
	# Delete old images
	cloudinary.api.delete_resources_by_prefix("raw_images")

	image_links = []
	for i in range(1, num_pages + 1):
		upload_ref = cloudinary.uploader.upload("raw_images/" + str(i) + ".png", use_filename=True, folder="raw_images")
		image_links.append(upload_ref['secure_url'])

	with open('poems.json', 'w') as f:
    	json.dump(image_links, f)

def retrieveImages():
	with open('poems.json', 'r') as f:
		image_links = json.load(f)
	return jsonify(image_links)


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

@app.route("/retrieve", methods = ['GET'])
def retrieve_images():
	if request.method == "GET":
		return retrieveImages()

# Driver function - must be at the end
if __name__ == '__main__': 
	app.run()