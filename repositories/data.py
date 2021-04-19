from sqlalchemy.exc import IntegrityError
from collections import defaultdict

from exceptions import ResourceExists, ResourceDoesNotExist
from models import HatModel, Colors, DataModel


class DataRepository:

    @staticmethod
    def create(data) -> dict:
        """ Create Hat """
        result: dict = {}
        try:

            sum = defaultdict(float)
            count = defaultdict(float)
            for d in data:
                sum[d['name']] += d['value']
                count[d['name']] += 1

            avg = defaultdict(float)

            for d in sum:
                avg[d] = sum[d] / count[d]

            for d in avg:

                d = DataModel(d, avg[d])
                d.save()

        except IntegrityError:
            HatModel.rollback()
            raise ResourceExists('hat already exists')

        return avg