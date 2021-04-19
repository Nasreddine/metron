from models import db, BaseModel
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func


class DataModel(db.Model, BaseModel):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    value = db.Column(db.Float)
    time_created = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, name, value):
        self.name = name
        self.value = value

