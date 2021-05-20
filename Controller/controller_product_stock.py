from flask_restful import Resource
from Utils.products import products_utils


class ControllerProductReportStock(Resource):

    @staticmethod
    def get():
        response = products_utils.get_all_products()
        return response