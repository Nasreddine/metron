from models import db, BaseModel
import enum

class Colors(enum.Enum):
    PURPLE: str = "PURPLE"
    YELLOW: str = "YELLOW"
    GREEN: str = "GREEN"

    def __str__(self):
        return self.value



class HatModel(db.Model, BaseModel):
    __tablename__ = 'hat'

    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.Enum(Colors, values_callable=lambda obj: [e.value for e in obj]),
                      nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'),
                             nullable=True)

    character = db.relationship("CharacterModel",
                                uselist=False,
                                backref="character",
                                lazy=True)

    def __init__(self, color: Colors):
        self.color = color
