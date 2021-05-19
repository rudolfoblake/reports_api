from Controller.health_check import HealthCheck
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

    api.init_app(app)
