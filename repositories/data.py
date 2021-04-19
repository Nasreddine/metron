from sqlalchemy.exc import IntegrityError
from collections import defaultdict

from exceptions import ResourceExists
from models import HatModel, DataModel


class DataRepository:

    @staticmethod
    def create(data) -> dict:
        """ Create Data """
        try:
            # Calculate sum and count by key
            sum = defaultdict(float)
            count = defaultdict(float)
            for d in data:
                sum[d['name']] += d['value']
                count[d['name']] += 1

            # Calculate average
            avg = defaultdict(float)
            for d in sum:
                avg[d] = sum[d] / count[d]
            # save each entry separately
            for d in avg:
                d = DataModel(d, avg[d])
                d.save()

        except IntegrityError:
            HatModel.rollback()
            raise ResourceExists('hat already exists')
        return avg
