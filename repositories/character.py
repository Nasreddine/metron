from sqlalchemy.exc import IntegrityError
from exceptions import ResourceDoesNotExist
from models import CharacterModel, HatModel
from repositories import *


class CharacterRepository:

    @staticmethod
    def get(id: int) -> dict:
        """ Query a character by id """
        character = CharacterModel.query.get_or_404(id)
        character = {
            "name": character.name,
            "age": character.age,
            "weight": character.weight,
            "human": character.human
        }
        return character

    @staticmethod
    def delete(id: int) -> dict:
        """ Query a character by id """
        character = CharacterModel.query.get_or_404(id)
        character.delete()
        result = {
            "deleted": True,
        }
        return result

    @staticmethod
    def get_all() -> dict:

        characters = CharacterModel.query.all()

        results = [
            {
                "name": character.name,
                "age": character.age,
                "weight": character.weight,
                "human": character.human
            } for character in characters]

        return {"count": len(results), "characters": results}

    @staticmethod
    def create(name: str, age: int, weight: float, human: bool, hat_id: int = None) -> dict:
        """ Create character """
        result: dict = {}
        try:
            # if hat_id is not None, check if exists, throw exception instead
            if hat_id is not None:
                hat = HatModel.query.get(hat_id)
                if hat is None:
                    raise ResourceDoesNotExist("Hat {} does not exist".format(hat_id))

            character = CharacterModel(name=name, age=age, weight=weight, human=human, hat_id=hat_id)
            character.save()

            result = {
                'id' : character.id,
                'name': character.name,
                'age': character.age,
                'weight': character.weight,
                'human': character.human,
                'hat_id': character.hat_id,
            }
        except IntegrityError:
            CharacterModel.rollback()
            # raise ResourceExists('Character already exists')


        return result

    @staticmethod
    def update(id: int, name: str, age: int, weight: float, human: bool, hat_id: int = None) -> dict:
        """ Create character """
        result: dict = {}
        try:
            character = CharacterModel.query.get(id)
            character.name = name
            character.age = age
            character.weight = weight
            character.human = human
            character.hat_id = hat_id

            CharacterModel.commit()

            result = {
                'id': character.id,
                'name': character.name,
                'age': character.age,
                'weight': character.weight,
                'human': character.human,
                'hat_id': character.hat_id,
            }
        except IntegrityError:
            CharacterModel.rollback()
            # raise ResourceExists('user already exists')

        return result


