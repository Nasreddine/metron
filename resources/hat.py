from flask import request, jsonify
from flask_restful import Resource

from models import Colors
from repositories import HatRepository


class HatResource(Resource):
    def get(self, id: int):
        hat = HatRepository.get(id)
        return hat, 200

    def delete(self, id: int):
        response = HatRepository.delete(id)

        return response, 200

    def put(self, id):
        """
        Update hat
        """
        request_json = request.get_json(silent=True)

        try:
            color: Colors = request_json['color']
            hat = HatRepository.update(id, color=color)
            return hat, 200

        except Exception as e:
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response


class HatListResource(Resource):

    def get(self):
        hats = HatRepository.get_all()
        return hats, 200

    def post(self):
        """
        Create Hat
        """
        request_json = request.get_json(silent=True)

        try:
            color: Colors = request_json['color']
            hat = HatRepository.create(color)
            return hat, 200

        except Exception as e:
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response
