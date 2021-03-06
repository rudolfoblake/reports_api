from datetime import datetime
from flask import request
from flask_restful import Resource
from Database.auth import KEYS
from Utils.products import products_utils


class ControllerProductReportProfit(Resource):

    @staticmethod
    def get():
        header = dict(request.headers)

        if "Access-Key" not in list(header.keys()) or header.get("Access-Key") not in list(KEYS.values()):
            response = dict(status=400, error="Chave de acesso inválida.", message="Verifique os dados informados.")
        else:
            body_request = {"report_header": {}, "report_body": {}}
            body_request["report_header"]["title"] = "Relatórios de margem de lucro por produtos"
            current_date = datetime.today()
            body_request["report_header"]["current_date"] = current_date.strftime("%d/%m/%Y, %H:%M")
            body_request["report_body"] = products_utils.get_all_products()
            body_request["report_body"] = products_utils.calculate_profit_by_product(body_request["report_body"])
            response = dict(body_request, status=200, message="ok")
        return response
