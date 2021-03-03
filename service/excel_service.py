#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/3 21:55
# @Author  : Gavin
# @File    : excel_service.py


import uuid

from constants import UPLOAD_ALLOWED_EXTENSIONS
from utils.excel_utils import HSSFUtils, XSSFUtils


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in UPLOAD_ALLOWED_EXTENSIONS


def process(folder, filename):
    suffix = filename.rsplit(".", 1)[1]
    excel_utils = HSSFUtils() if suffix == "xls" else XSSFUtils()
    read_all = excel_utils.read_all("%s/%s" % (folder, filename))
    new_file = "%s.%s" % (uuid.uuid4(), suffix)
    new_file_path = "%s/%s" % (folder, new_file)
    excel_utils.write_all(new_file_path, read_all)
    return new_file
