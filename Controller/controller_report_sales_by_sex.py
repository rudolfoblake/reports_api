from flask_restful import Resource
from flask import request
from Database.auth import KEYS


class ReportSalesBySex(Resource):

    @staticmethod
    def post():
        header = dict(request.headers)

        if "Access-Key" not in list(header.keys()) or header.get("Access-Key") not in list(KEYS.values()):
            response = dict(status=400, error="Chave de acesso inválida.", message="Verifique os dados informados.")
        else:
            body_request = {"report_header": request.get_json(), "report_body": None}
            body_request["report_header"]["title"] = "Relatórios de vendas por sexo"
            # response = book_controller.insert_book(body_request)
            response = dict(body_request, status=200, message="ok")
        return response
