#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/3 22:01
# @Author  : Gavin
# @File    : app.py


from flask import Flask

from constants import UPLOAD_FOLDER, UPLOAD_MAX_CONTENT_LENGTH
from route.index_route import index
from route.excel_route import excel

app = Flask(__name__)


app.register_blueprint(index, url_prefix="/index")
app.register_blueprint(excel, url_prefix="/excel")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = UPLOAD_MAX_CONTENT_LENGTH


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6011, debug=True)
