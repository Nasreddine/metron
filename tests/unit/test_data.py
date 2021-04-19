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
        d1 = DataModel(name="nasredine", value=10)
        d2 = DataModel(name="nasredine", value=10)
        d3 = DataModel(name="sid", value=10)

        data_array.append(d1)
        data_array.append(d2)
        data_array.append(d3)

        data_post = [
            {"name": v.name, "value": v.value,
             } for v in data_array]
        data_json = json.dumps({
            "data": data_post,
        })

        response = self.execute_post(data_json)

        print(response)

        self.assertEqual(10.0, response.json['nasredine'])
        self.assertEqual(10.0, response.json['sid'])

    def execute_post(self, data):
        """
           Perform POST request to /hats and return response
            """
        response = self.test_client.post('/data', headers={"Content-Type": "application/json"}, data=data)
        return response
