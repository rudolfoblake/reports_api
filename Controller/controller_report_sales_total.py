import json
from flask_restful import Resource
from flask import request
from Database.auth import KEYS, URL_SALES_API_ORDERS_REPORTS_1
from Utils.sales.utils_reports_extract_data import get_data_from_order_logs


class ReportSalesTotal(Resource):

    @staticmethod
    def post():
        header = dict(request.headers)

        if "Access-Key" not in list(header.keys()) or header.get("Access-Key") not in list(KEYS.values()):
            response = dict(status=400,
                            error="Chave de acesso inválida.",
                            message="Verifique os dados informados.")
        else:
            body_request = {"report_header": request.get_json(), "report_body": None}
            body_request["report_header"]["title"] = "Relatório geral de vendas"

            dates = dict(initial_date=body_request['report_header']['initial_date'],
                         final_date=body_request['report_header']['final_date'])

            data_info = get_data_from_order_logs(url=URL_SALES_API_ORDERS_REPORTS_1,
                                                 filter_data=dates)

            body_request["report_body"] = json.loads(data_info['data'])

            response = dict(body_request,
                            status=200,
                            message="ok")
        return response
