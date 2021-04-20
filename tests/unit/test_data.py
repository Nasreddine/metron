import unittest
import json

from main import app
from models import db, DataModel


class DataTest(unittest.TestCase):

    def setUp(self):
        self.test_client = app.test_client()
        self.app = app
        self.db = db

    def test_successful_create(self):
        """
        GIVEN a Flask application
        WHEN the '/data' endpoint is is posted with array of data
        THEN check that results are correct
        """

        data_array = []
        d1 = DataModel(name="nasredine", value=2.347736)
        d2 = DataModel(name="nasredine", value=13.763882)
        d3 = DataModel(name="sid", value=10)

        data_array.append(d1)
        data_array.append(d2)
        data_array.append(d3)

        data_dict = [
            {
                "name": v.name, "value": v.value,
            } for v in data_array]

        data_json = json.dumps({
            "data": data_dict,
        })

        response = self.execute_post(data_json)

        self.assertAlmostEqual(8.05, response.json['nasredine'],1)
        self.assertAlmostEqual(10.0, response.json['sid'],1)

    def execute_post(self, data):
        """
           Perform POST request to /hats and return response
            """
        response = self.test_client.post('/data', headers={"Content-Type": "application/json"}, data=data)
        return response

    def almost_equal(self, value_1, value_2, accuracy=10 ** -8):
        return abs(value_1 - value_2) < accuracy
