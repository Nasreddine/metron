from sqlalchemy.exc import IntegrityError

from exceptions import ResourceExists
from models import HatModel, Colors


class HatRepository:

    @staticmethod
    def create(color: Colors) -> dict:
        """ Create Hat """
        result: dict = {}
        try:
            hat = HatModel(color=color)
            hat.save()
            result = {
                'id': hat.id,
                'color': color
            }
        except IntegrityError:
            HatModel.rollback()
            raise ResourceExists('hat already exists')

        return result

    @staticmethod
    def update(id: int, color: Colors) -> dict:
        """ Create character """
        result: dict = {}
        try:
            hat = HatModel.query.get(id)
            hat.color = color
            HatModel.commit()

            result = {
                'id': hat.id,
                'color': hat.color.value,
            }
        except IntegrityError:
            HatModel.rollback()
            # raise ResourceExists('user already exists')

        return result

    @staticmethod
    def delete(id: int) -> dict:
        """ Query a character by id """
        character = HatModel.query.get_or_404(id)
        character.delete()
        result = {
            "deleted": True,
        }
        return result

    @staticmethod
    def get(id: int) -> dict:
        """ Query a user by username """
        hat = HatModel.query.get_or_404(id)
        hat = {
            "color": hat.color.value,
            "character_id": hat.character_id,
        }
        return hat

    @staticmethod
    def get_all() -> dict:
        hats = HatModel.query.all()

        results = [
            {
                "id": hat.id,
                "color": hat.color.value,
            } for hat in hats]

        return {"count": len(results), "hats": results}
