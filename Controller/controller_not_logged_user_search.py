from datetime import datetime

from flask import request
from flask_restful import Resource
from Database.auth import KEYS


class ControllerNotLoggedUserSearchReport(Resource):

    @staticmethod
    def get():
        header = dict(request.headers)

        if "Access-Key" not in list(header.keys()) or header.get("Access-Key") not in list(KEYS.values()):
            response = dict(status=400, error="Chave de acesso inválida.", message="Verifique os dados informados.")
        else:
            body_request = {"report_header": {}, "report_body": {}}
            body_request["report_header"]["title"] = "Relatórios de tags mais pesquisadas por usuários não logados"
            current_date = datetime.today()
            body_request["report_header"]["current_date"] = current_date.strftime("%d/%m/%Y, %H:%M")
            body_request["report_body"] = search_engine_utils.get_all_searches_by_user_not_logged()
            response = dict(body_request, status=200, message="ok")
        return response