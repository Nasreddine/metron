from flask_sqlalchemy import SQLAlchemy
from .hat import HatRepository
from .character import CharacterRepository
from .data import DataRepository

db = SQLAlchemy()
__all__ = ['CharacterRepository','HatRepository', 'DataRepository']