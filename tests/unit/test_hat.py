import unittest
import json

from main import app
from models import db, Colors


class HatTest(unittest.TestCase):

    def setUp(self):
        self.test_client = app.test_client()
        self.app = app
        self.db = db

    def test_successful_create(self):
        """
        GIVEN a Flask application
        WHEN the '/characters' endpoint is is posted to create a new valid character
        THEN check that a '200' status code is returned
        """

        hat = json.dumps({
            "color": "YELLOW",
        })

        response = self.execute_post(hat)

        self.assertEqual("YELLOW", response.json['color'])
        self.assertEqual(200, response.status_code)

    def execute_post(self, data):
        """
           Perform POST request to /characters and return response
            """
        response = self.test_client.post('/hats', headers={"Content-Type": "application/json"}, data=data)
        return response

    def test_delete_hat(self):
        """
                  GIVEN a Flask application
                  WHEN the '/hat' endpoint is is posted to create a character without a hat,
                  THEN check that a '200' status code is returned
                  """

        hat = json.dumps({
            "color": "YELLOW",
        })

        response = self.execute_post(hat)
        hat_id = response.json['id']

        response = self.execute_delete(hat_id)

        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json['deleted'])

    # TODO: refactr code, put common methods in super class
    def execute_delete(self, id):
        response = self.test_client.delete('/hat/{}'.format(id), headers={"Content-Type": "application/json"})
        return response
