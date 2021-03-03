#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/3 21:55
# @Author  : Gavin
# @File    : index_route.py


from flask import Blueprint, render_template, redirect

index = Blueprint("index", __name__)


@index.route("/", methods=["GET", "POST"])
def home():
    return redirect(location="/index/upload")


@index.route("/upload", methods=["GET", "POST"])
def upload_page():
    return render_template("excel_upload.html")
