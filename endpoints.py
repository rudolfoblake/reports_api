from Controller.controller_health_check import HealthCheck
from Controller.controller_report_sales_most_sold_item import ReportSalesMostSoldItem
from Controller.controller_report_sales_total import ReportSalesTotal
from Controller.controller_report_sales_by_age import ReportSalesByAge
from Controller.controller_report_sales_by_sex import ReportSalesBySex
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
    api.add_resource(ReportSalesMostSoldItem, "/reports/sales/most_sold_item")
    api.add_resource(ReportSalesByAge, "/reports/sales/by_age")
    api.add_resource(ReportSalesBySex, "/reports/sales/by_sex")
    api.add_resource(ReportSalesTotal, "/reports/sales/total")
    api.add_resource(ControllerProductReportStock, "/reports/product/stock-report")
    api.add_resource(ControllerProductReportProfit, "/reports/product/profit-report")
    api.add_resource(ControllerLoggedInUserSearchReport, "/reports/product/profit-report")
    api.add_resource(ControllerNotLoggedUserSearchReport, "/reports/product/profit-report")

    api.init_app(app)
