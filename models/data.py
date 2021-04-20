from collections import defaultdict

from models import db, BaseModel
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func


class DataModel(db.Model, BaseModel):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    value = db.Column(db.Float)
    # Initializes time_created date to the current time
    time_created = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, name, value):
        self.name = name
        self.value = value

    @classmethod
    def compute_average_values(cls, data):
        # for each name, we calculate sum and we count number of values
        sum_of_values = defaultdict(float)
        count_of_values = defaultdict(float)

        for d in data:
            sum_of_values[d['name']] += d['value']
            count_of_values[d['name']] += 1

        # Calculate average
        avg_values = defaultdict(float)
        for d in sum_of_values:
            avg_values[d] = sum_of_values[d] / count_of_values[d]

        return avg_values
