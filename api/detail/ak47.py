from flask.views import MethodView
from flask import request
from flask_restful import inputs, reqparse
class Search(MethodView):
    parser = reqparse.RequestParser()
    parser.add_argument("key", type=str)
    parser.add_argument("value", type=str)

    def __init__(self):
        #
        print("???")

    def post(self, uid: str = None):
        request.get_json(force=True)
        args = self.parser.parse_args()
        print("what can i say? \n")
        print(args["choice"],'\n')
        # return to_json(dag, {"dag_type": "type"})