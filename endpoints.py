from Controller.health_check_controller import HealthCheck
from Controller.controller_product_profit import ControllerProductReportProfit
from Controller.controller_product_stock import ControllerProductReportStock
from flask_restful import Api


def init_api(app):
    """
    Function that executes on the initiation of the API and
    connect the controller classes with the respective routes.

    :param app: main app
    :return: API initialization
    """
    api = Api()

    api.add_resource(HealthCheck, "/health-check")
    api.add_resource(ControllerProductReportStock, "/reports/product/stock-report")
    api.add_resource(ControllerProductReportProfit, "/reports/product/profit-report")
    

    api.init_app(app)