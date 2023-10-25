from flask import (Blueprint, render_template, request, flash, redirect, 
                   send_from_directory, url_for)
from dotenv import dotenv_values
from werkzeug.utils import secure_filename
import os

config = dotenv_values(".env")

bp = Blueprint("file_handler", __name__)

@bp.route("/file-handler", methods=['GET', 'POST'])
def file_handler():
    if request.method == 'POST':
        print(request)
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(config['TMP'], filename))
            return redirect(request.url)
    if request.method == 'GET':
        form_id = request.form.get("id", "")
        if form_id == "download":
            return redirect(url_for("/file-handler/download", request.form['text']))

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    <h1>Download a file</h1>
    <form name=download method=get enctype=multipart/form-data>
      <input type="hidden" value="download" name="id">
      <input type=text name=download>
      <input type=submit value=Download>
    </form>
    ''' 

@bp.route('/file-handler/download/<name>')
def download_file(name):
    print(name)
    return send_from_directory(config["TMP"], name)        