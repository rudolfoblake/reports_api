import json
from flask_restful import Resource
from flask import request
from Database.auth import KEYS
from Utils.sales.utils_reports_extract_data import get_data_from_order_logs
from Utils.sales.utils_reports_convert_data import convert_log_data


class ReportSalesMostSoldItem(Resource):

    @staticmethod
    def post():
        header = dict(request.headers)

        if "Access-Key" not in list(header.keys()) or header.get("Access-Key") not in list(KEYS.values()):
            response = dict(status=400, error="Chave de acesso inválida.", message="Verifique os dados informados.")
        else:
            body_request = {"report_header": request.get_json(), "report_body": None}
            body_request["report_header"]["title"] = "Relatório de itens mais vendidos"

            dates = dict(initial_date=body_request["report_header"]["initial_date"],
                         final_date=body_request["report_header"]["final_date"])

            data_info = get_data_from_order_logs(url="http://127.0.0.1:8000/orders/reports/2",
                                                 filter_data=dates)

            if data_info["status"] is False:
                response = dict(status=500, error="Dados incorretos.", message=data_info["message"])
            else:
                try:
                    result_list = convert_log_data(json.loads(data_info["data"]))
                    body_request["report_body"] = result_list

                    response = dict(body_request,
                                    status=200,
                                    message="ok")
                except KeyError:
                    response = dict(status=400,
                                    error="Chave inválida.",
                                    message="Problema na lista de produtos.")

        return response
