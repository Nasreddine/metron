from . import db


class BaseModel:
    def save(self):
        self.validate()
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self
    
    def validate(self):
        return True

    @staticmethod
    def rollback():
        db.session.rollback()

    @staticmethod
    def commit():
        db.session.commit()
