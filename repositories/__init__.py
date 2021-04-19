from flask_sqlalchemy import SQLAlchemy
from .hat import HatRepository
from .character import CharacterRepository


db = SQLAlchemy()
__all__ = ['CharacterRepository','HatRepository']