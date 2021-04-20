from flask import request, jsonify
from flask_restful import Resource

from repositories import CharacterRepository


class CharacterResource(Resource):
    def get(self, id: int):
        character = CharacterRepository.get(id)
        return character, 200

    def delete(self, id: int):
        response = CharacterRepository.delete(id)

        return response, 200

    def put(self, id):
        """
        Create Character
        """
        request_json = request.get_json(silent=True)

        try:
            name: str = request_json['name']
            age: int = request_json['age']
            weight: float = request_json['weight']
            human: bool = request_json['human']
            hat_id: bool = request_json['hat_id']

            character = CharacterRepository.update(id, name, age, weight, human, hat_id)
            return character, 200

        except Exception as e:
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response


class CharacterListResource(Resource):
    """
           A class that provides abstract access to list of characters
           It provides also post request method to create character

           """

    def get(self):
        characters = CharacterRepository.get_all()
        return characters, 200

    def post(self):
        """
        Create Character
        """
        request_json = request.get_json(silent=True)

        try:
            name: str = request_json['name']
            age: int = request_json['age']
            weight: float = request_json['weight']
            human: bool = request_json['human']
            hat_id: bool = request_json['hat_id']

            character = CharacterRepository.create(name, age, weight, human, hat_id)
            return character, 200

        except Exception as e:
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response
