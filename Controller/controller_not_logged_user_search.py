from datetime import datetime

import requests
from flask import request, jsonify
from flask_restful import Resource
import json

from Database.auth import KEYS
from Utils.search_engine import search_engine_utils


class ControllerNotLoggedUserSearchReport(Resource):

    @staticmethod
    def post():
        header = dict(request.headers)

        if "Access-Key" not in list(header.keys()) or header.get("Access-Key") not in list(KEYS.values()):
            response = dict(status=400, error="Chave de acesso inválida.", message="Verifique os dados informados.")
        else:
            body_request = {"report_header": {}, "report_body": {}}
            body_request["report_header"]["title"] = "Relatórios de tags mais pesquisadas por usuários não logados"
            current_date = datetime.today()
            body_request["report_header"]["current_date"] = current_date.strftime("%d/%m/%Y, %H:%M")
            request_body = request.get_json(force=True)
            dates = dict(initial_date=request_body["initial_date"], final_date=request_body["final_date"])
            body_request["report_body"] = search_engine_utils.get_not_logged_users_report(dates)
            response = dict(body_request, status=200, message="ok")
        return response
