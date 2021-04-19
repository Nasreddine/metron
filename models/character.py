from repositories import *
from . import db, Colors, HatModel
from .base_model import BaseModel
from exceptions import ValidationError


class CharacterModel(db.Model, BaseModel):
    __tablename__ = 'character'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    weight = db.Column(db.Float())
    human = db.Column(db.Boolean())
    hat_id = db.Column(db.Integer())
    hat = db.relationship("HatModel", uselist=False, backref="hat", lazy=True, cascade="all,delete")
    # car = db.relationship("Car", uselist=False, back_populates="car")

    def __init__(self, name: str, age: int, weight: float, human: bool = False, hat_id: int = None):

        self.name = name
        self.weight = weight
        self.age = age
        self.human = human
        self.hat_id = hat_id
        self.hat = self.hat
        if hat_id is not None:
            # self.hat = HatRepository.get(hat_id)
            # TOFIX: use repository after resolving cyclic import errors
            self.hat = HatModel.query.get(hat_id)


    """ Separate validations deponding on Model """

    def validate(self):
        self.validate_human_age_weight()
        self.validate_human_hat()
        self.validate_name_hat_color()
        return True

    def validate_human_age_weight(self):
        if self.age <= 0:
            raise ValidationError("Age must be greater than 0")
        if self.weight > 80 and self.is_human() and self.age < 10:
            raise ValidationError("Age must be greater than 10")
        return True

    def validate_human_hat(self):
        if (not self.is_human()) and (self.hat is not None):
            raise ValidationError("Not human, no hat!")

    def validate_name_hat_color(self):
        if (self.is_human()
                and "p" in self.name.lower()
                and self.hat is not None
                and self.hat.color == Colors.YELLOW):
            raise ValidationError("Names containing p, cannot have a YELLOW Hat!")

    def is_human(self):
        return self.human is True

    def __repr__(self):
        return f"<Character {self.name}>"
