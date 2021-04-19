import unittest
import json

from main import app
from models import db, Colors


class CharacterTest(unittest.TestCase):

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

        character = json.dumps({
            "name": "nasredine",
            "age": 10,
            "weight": 85,
            "human": True,
            "hat_id": None,
        })

        response = self.execute_post(character)

        self.assertEqual("nasredine", response.json['name'])
        self.assertEqual(200, response.status_code)

    def test_successful_update(self):
        """
        GIVEN a Flask application
        WHEN the '/characters' endpoint is is posted to create a new valid character
        THEN check that a '200' status code is returned
        """

        character = json.dumps({
            "name": "nasredine",
            "age": 10,
            "weight": 85,
            "human": True,
            "hat_id": None,
        })

        response = self.execute_post(character)

        self.assertEqual("nasredine", response.json['name'])
        self.assertEqual(200, response.status_code)

        character_updated = json.dumps({
            "name": "nasredine CHENIKI",
            "age": 10,
            "weight": 85,
            "human": True,
            "hat_id": None,
        })

        response_put = self.execute_put(response.json['id'], character_updated)

        self.assertEqual("nasredine CHENIKI", response_put.json['name'])
        self.assertEqual(200, response_put.status_code)

    def test_negative_age(self):
        """
              GIVEN a Flask application
              WHEN the '/characters' endpoint is is posted to create non-valid character (negative age)
              THEN check that a '400' status code is returned
              """
        character = json.dumps({
            "name": "nasredine",
            "age": -10,
            "weight": 85,
            "human": True,
            "hat_id": None,
        })

        response = self.execute_post(character)

        self.assertEqual(400, response.status_code)
        self.assertEqual("Age must be greater than 0", response.json['message'])

    def test_weight_age_consistency(self):
        """
                   GIVEN a Flask application
                   WHEN the '/characters' endpoint is is posted to create non-valid character (age and weight inconsistency)
                   THEN check that a '400' status code is returned
                   """

        character = json.dumps({
            "name": "nasredine",
            "age": 5,
            "weight": 85,
            "human": True,
            "hat_id": None,
        })

        response = self.execute_post(character)

        self.assertEqual("Age must be greater than 10", response.json['message'])
        self.assertEqual(400, response.status_code)

    def test_create_character_with_not_existing_hat(self):
        """
        GIVEN a Flask application
        WHEN the '/characters' endpoint is is posted to create a character with a hat that doesn't exist
        THEN check that a '404' status code is returned
        """
        hat_id = 5000
        character = json.dumps({
            "name": "nasredine",
            "age": 50,
            "weight": 85,
            "human": True,
            "hat_id": hat_id,
        })

        response = self.execute_post(character)

        # TODO: put each exception error into its own Class
        self.assertEqual(404, response.status_code)
        self.assertEqual("Hat {} does not exist".format(hat_id), response.json['message'])


    def test_create_character_has_p_in_name_and_has_yellow_hat(self):
        """
              GIVEN a Flask application
              WHEN the '/characters' endpoint is is posted to create a character that has p in his name, and has a yellow hat!
              THEN check that a '400' status code is returned
              """

        hat = json.dumps({
            "color": "YELLOW"
        })

        hat_response = self.test_client.post('/hats', headers={"Content-Type": "application/json"}, data=hat)

        character = json.dumps({
            "name": "Peter",
            "age": 50,
            "weight": 85,
            "human": True,
            "hat_id": hat_response.json["id"]
        })

        response = self.execute_post(character)

        self.assertEqual(400, response.status_code)
        self.assertEqual("Names containing p, cannot have a YELLOW Hat!", response.json['message'])

    def test_delete_character_without_hat(self):
        """
                  GIVEN a Flask application
                  WHEN the '/characters' endpoint is is posted to create a character without a hat,
                  THEN check that a '200' status code is returned
                  """

        character = json.dumps({
            "name": "nasredine",
            "age": 31,
            "weight": 65,
            "human": True,
            "hat_id": None,
        })

        response = self.execute_post(character)
        character_id = response.json['id']

        response = self.execute_delete(character_id)

        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json['deleted'])

    def test_delete_character_with_a_hat(self):
        """
                     GIVEN a Flask application
                     WHEN the '/characters' endpoint is is posted to create a character with a hat,
                     THEN check that a '200' status code is returned
                     """

        hat = json.dumps({
            "color": "GREEN"
        })

        response_create_hat = self.test_client.post('/hats', headers={"Content-Type": "application/json"}, data=hat)
        hat_id = response_create_hat.json["id"]

        character = json.dumps({
            "name": "Nasredine",
            "age": 50,
            "weight": 85,
            "human": True,
            "hat_id": hat_id
        })

        response_create_character = self.execute_post(character)
        response_delete_character = self.execute_delete(response_create_character.json["id"])

        response_get_hat = self.test_client.get('/hat/{}'.format(hat_id), headers={"Content-Type": "application/json"})

        self.assertEqual(200, response_create_character.status_code)
        self.assertEqual(200, response_delete_character.status_code)
        self.assertEqual(404, response_get_hat.status_code)

    # def tearDown(self):
    # # Delete Database collections after the test is complete
    #     with self.app.app_context():
    #         self.db.session.commit()
    #         self.db.drop_all()
    #         self.metadata.create_all()

    def execute_post(self, data):
        """
           Perform POST request to /characters and return response
            """
        response = self.test_client.post('/characters', headers={"Content-Type": "application/json"}, data=data)
        return response

    def execute_delete(self, id):
        response = self.test_client.delete('/character/{}'.format(id), headers={"Content-Type": "application/json"})
        return response

    def execute_put(self, id, data):
        response = self.test_client.put('/character/{}'.format(id), headers={"Content-Type": "application/json"},data=data)
        return response
