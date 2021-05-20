from flask_restful import Resource


class HealthCheck(Resource):
    """
    Class Health check, to check the functionality of the API
    :return a ok and 200 http response
    """
    @staticmethod
    def get():
        return 'ok', 200
