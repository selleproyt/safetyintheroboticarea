from flask import Flask
from flask import request
from flask import render_template, redirect, flash, url_for
from base import takeuser
from flask import session
import os
import urllib.request
app = Flask(__name__,static_folder="static")
app.config['SECRET_KEY']="5b38897f6f7b7bb3fcb2c8a55027235710df24b1"
UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'mp4',"MP4"}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template('main2.html')



@app.route("/submitnetwork", methods=['POST'])
def submitnetwork():
    file = request.files['video']
    if file:
        filename = (file.filename)
        file.save(filename)
    problems=["Человек без каски Accuracy:0.6","Открыта дверь Accuracy:0.6"]
    dlp=len(problems)
    return render_template('main.html',problems=problems,dlp=dlp)


#print()
app.run()