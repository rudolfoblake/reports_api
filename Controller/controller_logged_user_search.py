from flask import request
from flask_restful import Resource
from Database.auth import KEYS


class ControllerLoggedInUserSearchReport(Resource):

    @staticmethod
    def get():
        header = dict(request.headers)

        if "Access-Key" not in list(header.keys()) or header.get("Access-Key") not in list(KEYS.values()):
            response = dict(status=400, error="Chave de acesso inválida.", message="Verifique os dados informados.")
        else:
            pass
        return response