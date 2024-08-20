from typing import Type

from flask import Blueprint
from flask.views import MethodView


def url(bp: Blueprint, rule: str, method_view: Type[MethodView],
        view_name: str = None,
        methods: list = ("GET", "POST", "DELETE")):
    if view_name is None:
        view_name = method_view.__name__
    bp.add_url_rule(rule, view_func=method_view.as_view(view_name),
                    methods=methods)
