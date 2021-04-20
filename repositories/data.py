from sqlalchemy.exc import IntegrityError
from collections import defaultdict

from exceptions import ResourceExists
from models import HatModel, DataModel


class DataRepository:
    """
          A class to provide query interface to Data model

          """

    @staticmethod
    def create(data) -> dict:
        """ Create Data """
        try:

            avg_values = DataModel.compute_average_values(data)

            # save each entry separately
            for d in avg_values:
                d = DataModel(d, avg_values[d])
                d.save()

        except IntegrityError:
            DataModel.rollback()
            raise ResourceExists('hat already exists')
        return avg_values
