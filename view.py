# MVC
# db - model
# view - conroller
# Templates(шаблоны) - отображение view
import os
from app import app
from flask import render_template
from flask import Flask, flash, request, redirect, url_for

import librosa

import matplotlib.pyplot as plt
import librosa.display

UPLOAD_FOLDER = '/home/ubuntualex/cft/CFT_test_audio_web/temp/'
ALLOWED_EXTENSIONS = {'mp3'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def uploaded_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename # Уязвимость
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            audio_data = UPLOAD_FOLDER + filename
            x , sr = librosa.load(audio_data)
            
            plt.figure(figsize=(14, 2))
            librosa.display.waveplot(x, sr=sr)
            plt.savefig('static/graph_temp.png')

            # return redirect(url_for('uploaded_file', filename=filename))
            return render_template('image.html')
    return render_template('index.html')