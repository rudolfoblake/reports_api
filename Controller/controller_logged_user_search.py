from datetime import datetime
from flask import request
from flask_restful import Resource
from Database.auth import KEYS
from Utils.search_engine import search_engine_utils
from Utils.search_engine.search_engine_utils import GET_LOGGED_USERS_REPORT


class ControllerLoggedInUserSearchReport(Resource):

    @staticmethod
    def post():
        header = dict(request.headers)

        if "Access-Key" not in list(header.keys()) or header.get("Access-Key") not in list(KEYS.values()):
            response = dict(status=400, error="Chave de acesso inválida.", message="Verifique os dados informados.")
        else:
            body_request = {"report_header": {}, "report_body": {}}
            body_request["report_header"]["title"] = "Relatórios de tags mais pesquisadas por usuários logados"
            current_date = datetime.today()
            body_request["report_header"]["current_date"] = current_date.strftime("%d/%m/%Y, %H:%M")
            request_body = request.get_json(force=True)
            dates = dict(initial_date=request_body["initial_date"], final_date=request_body["final_date"])
            body_request["report_body"] = search_engine_utils.get_reports(dates, GET_LOGGED_USERS_REPORT)
            response = dict(body_request, status=200, message="ok")
        return response
