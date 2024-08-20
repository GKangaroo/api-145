#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

from api.util import url
from api.detail.ak47 import Search

detail = Blueprint("detail", __name__, url_prefix="/api/detail")

url(detail, "/search", Search.as_view('search'), view_name=('search'),methods=["POST"])

