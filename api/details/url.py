#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

from api.util import url
from api.details import Search

detail = Blueprint("detail", __name__, url_prefix="/api/detail")

url(detail, "/search", Search, methods=["POST"])

