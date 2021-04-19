from flask import request, jsonify
from flask_restful import Resource

from models import Colors
from repositories import HatRepository, CharacterRepository
from repositories.data import DataRepository


class DataResource(Resource):
    def post(self):
        """
        Create Data
        """
        request_json = request.get_json(silent=True)

        try:
            data = request_json['data']
            data_ = DataRepository.create(data)
            return data_, 200

        except Exception as e:
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response