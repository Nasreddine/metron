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
        WHEN the '/hats' endpoint is is posted to create a new hat
        THEN check that a '200' status code is returned
        """

        hat = json.dumps({
            "color": "YELLOW",
        })

        response = self.execute_post(hat)

        self.assertEqual("YELLOW", response.json['color'])
        self.assertEqual(200, response.status_code)

    def test_successful_update(self):
        """
        GIVEN a Flask application
        WHEN the '/hats' endpoint is is posted to update a hat
        THEN check that a '200' status code is returned
        """

        hat = json.dumps({
            "color": "YELLOW",
        })

        response = self.execute_post(hat)

        self.assertEqual("YELLOW", response.json['color'])
        self.assertEqual(200, response.status_code)

        hat_updated = json.dumps({
            "color": "GREEN",
        })

        response_put = self.execute_put(response.json['id'], hat_updated)

        self.assertEqual("GREEN", response_put.json['color'])
        self.assertEqual(200, response_put.status_code)

    def test_delete_hat(self):
        """
                  GIVEN a Flask application
                  WHEN the '/hat' endpoint is is posted to delete a hat,
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

    def execute_post(self, data):
        """
           Perform POST request to /hats and return response
            """
        response = self.test_client.post('/hats', headers={"Content-Type": "application/json"}, data=data)
        return response


    def execute_delete(self, id):
        response = self.test_client.delete('/hat/{}'.format(id), headers={"Content-Type": "application/json"})
        return response

    def execute_put(self, id, data):
        response = self.test_client.put('/hat/{}'.format(id), headers={"Content-Type": "application/json"},
                                        data=data)
        return response
