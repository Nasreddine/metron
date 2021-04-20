from . import db


class BaseModel:
    """
       A base class for models

       """
    def save(self):
        """Save model instance into database, instance must be valided first """
        self.validate()
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        """Delete model instance into database """
        db.session.delete(self)
        db.session.commit()
        return self
    
    def validate(self):
        """Validate model instance, can be overridden by subclasses """
        return True

    @staticmethod
    def rollback():
        """Rollback changes of model instance """
        db.session.rollback()

    @staticmethod
    def commit():
        """Commit changes of model instance to database """
        db.session.commit()
