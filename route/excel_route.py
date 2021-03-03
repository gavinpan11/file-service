#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/3 21:55
# @Author  : Gavin
# @File    : excel_route.py


import os

from flask import Blueprint, request, send_from_directory, render_template
from werkzeug.utils import secure_filename

from constants import PROJECT_ROOT, UPLOAD_FOLDER
from service import excel_service
from utils import file_utils


excel = Blueprint("excel", __name__)


@excel.route("/process", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file and excel_service.allowed_file(file.filename):
            new_file = None
            try:
                filename = secure_filename(file.filename)
                folder = "%s/%s" % (PROJECT_ROOT, UPLOAD_FOLDER)
                file.save(os.path.join(folder, filename))
                new_temp = excel_service.process(folder, filename)
                file_utils.delete("%s/%s" % (folder, filename))
                return send_from_directory("%s/%s" % (PROJECT_ROOT, UPLOAD_FOLDER), new_temp, as_attachment=True)
            finally:
                if new_file:
                    file_utils.delete(new_file)
    return render_template("excel_upload.html")
