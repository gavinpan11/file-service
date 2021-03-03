#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/3 21:55
# @Author  : Gavin
# @File    : constants.py


import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = "temp"
UPLOAD_ALLOWED_EXTENSIONS = {"xls", "xlsx"}
UPLOAD_MAX_CONTENT_LENGTH = 16 * 1024 * 1024
