from flask_restful import Resource
from flask import request
from Database.auth import KEYS
from Utils.utils_reports_sales_validations import validate_age_range


class ReportSalesByAge(Resource):

    @staticmethod
    def post():
        header = dict(request.headers)

        if "Access-Key" not in list(header.keys()) or header.get("Access-Key") not in list(KEYS.values()):
            response = dict(status=400, error="Chave de acesso inválida.", message="Verifique os dados informados.")
        else:
            body_request = {"report_header": request.get_json(), "report_body": None}
            body_request["report_header"]["title"] = "Relatório de vendas por faixa etária"

            if body_request["report_header"]["age"] < 0 or body_request["report_header"]["age"] > 121:
                response = dict(status=400, error="Idade inválida.", message="Verifique os dados informados.")
            else:
                body_request["report_header"]["age_range"] = validate_age_range(body_request["report_header"]["age"])
                del body_request["report_header"]["age"]
                body_request["report_body"] = None
                response = dict(body_request, status=200, message="ok")

        return response
