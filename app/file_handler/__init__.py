from flask import (Blueprint, render_template, request, flash, redirect, 
                   send_from_directory, url_for, send_file)
from dotenv import dotenv_values
from werkzeug.utils import secure_filename
import os
from utils.sqlite_tools.conversions import csv2sqlite as c2s

config = dotenv_values(".env")

bp = Blueprint("file_handler", __name__)

@bp.route("/file-handler", methods=['GET', 'POST'])
def file_handler():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join("app", config['TMP'], filename))
            return redirect(request.url)
    if request.method == 'GET':
        args_id = request.args.get("id", "")
        if args_id == "download":
            return redirect("/file-handler/download/" + request.args.get(args_id, ""))
        elif args_id == "convert":
            return redirect("/file-handler/convert/" + request.args.get(args_id, ""))
        

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
    <h1>Convert a file to db (csv, tsv, psv)</h1>
    <form name=convert method=get enctype=multipart/form-data>
      <input type="hidden" value="convert" name="id">
      <input type=text name=convert>
      <input type=submit value=Convert>
    </form>
    ''' 

@bp.route('/file-handler/convert/<name>')
def convert(name):
    print("converting")
    c2s.csv2sqlite(os.path.join("app", config["TMP"], name))
    return redirect("/file-handler")

@bp.route('/file-handler/download/<name>')
def download_file(name):
    if os.path.isfile(os.path.join("app", config["TMP"], name)):
        return send_from_directory(config["TMP"], name)        
    else:
        print("That file does not exist")
        # flash("That file does not exist")
    return redirect('/file-handler')