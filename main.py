import os, view
from app import app
from mp3 import graph_builder
# from flask import Flask, flash, request, redirect, url_for

# UPLOAD_FOLDER = '/home/ubuntualex/cft/CFT_test_audio_web/temp/'
# ALLOWED_EXTENSIONS = {'mp3'}

if __name__ == '__main__':
    
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.run(debug=True, host="0.0.0.0")
# from werkzeug.utils import secure_filename

# import librosa

# import matplotlib.pyplot as plt
# import librosa.display

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/', methods=['GET', 'POST'])
# def uploaded_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit an empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = file.filename # Уязвимость
            
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             audio_data = UPLOAD_FOLDER + filename
#             x , sr = librosa.load(audio_data)
            
#             plt.figure(figsize=(14, 5))
#             librosa.display.waveplot(x, sr=sr)
#             plt.savefig('books_read.png')

#             return redirect(url_for('uploaded_file', filename=filename))

#     return '''
#     <!doctype html>
#     <title>CFT</title>
#     <h1>Загрузите свой файл формата mp3</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload MP3>
#     </form>
#     '''