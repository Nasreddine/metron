from flask_restful import Api
from resources import HealthCheck, \
     CharacterResource, CharacterListResource, HatResource, HatListResource
from models import db, CharacterModel, HatModel
from flask_migrate import Migrate
from app import create_app

# App
app = create_app()
migrate = Migrate(app, db)

# API
api = Api(app)
api.add_resource(HealthCheck, '/healthcheck')
api.add_resource(CharacterListResource, '/characters',  endpoint = '/characters')
api.add_resource(CharacterResource, '/character/<int:id>',endpoint = 'character')
api.add_resource(HatResource, '/hat', '/hat/<id>')
api.add_resource(HatListResource, '/hats',  endpoint = '/hats')

# CLI for migrations

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, 
    CharacterResource=CharacterModel,
    HatResource=HatModel
    )