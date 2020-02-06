from flask_restful import Resource, reqparse
from models.especialidade_models import Especialidade_Model

class Especialidade_all(Resource):
    def get(self):
        return {'especialidades': [especi.json() for especi in Especialidade_Model.query.all()]}

class Especialide_Specific(Resource):
    def get(self, especialidade):
        pesquisa = Especialidade_Model.find_especi(especialidade)
        if pesquisa:
            return pesquisa.json()
        return {'message': 'Especialidade not found'}, 404

    def post(self, especialidade):
        pesquisa = Especialidade_Model.find_especi(especialidade)
        if pesquisa:
            return {'message': 'Essa Especialidade já existe.'}, 404

        especialidade = Especialidade_Model(especialidade)
        try:
            especialidade.save_especi()
        except:
            return {'message': 'error internal'}, 500
        return especialidade.json()

class Especi_By_Id(Resource):
    def get(self, especi_id):
        especialidade = Especialidade_Model.find_by_id(especi_id)
        if especialidade:
            return especialidade.json()
        return {'message': 'especialidade not found'}, 404

