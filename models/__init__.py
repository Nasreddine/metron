# flake8: noqa
# TODO: check if there is a better way
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .base_model import BaseModel
from .hat import HatModel,Colors

from .character import CharacterModel

__all__ = ['BaseModel','CharacterModel', 'HatModel', 'Colors']