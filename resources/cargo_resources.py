from flask_restful import Resource, reqparse, request
from models.cargo_models import Cargo_Model

class Cargo_all(Resource):
    def get(self):
        return {'cargos': [cargo.json() for cargo in Cargo_Model.query.all()]}

class Cargo_Specific(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('salario', type=float, required=True, help="The field 'float' cannot be left blank.")

    def get(self, nome):
        cargo = Cargo_Model.find_cargo(nome)
        if cargo:
            return cargo.json()
        return {'message': 'cargo not found.'}, 404 # not found

    def post(self, nome):
        if Cargo_Model.find_cargo(nome):
            return {"message": "The cargo '{}' already exists.".format(nome)}, 400 # bad request
        
        dados = Cargo_Specific.atributos.parse_args()
        cargo = Cargo_Model(nome, **dados)

        try:
            cargo.save_cargo()
        except:
            return {'message': 'An internal error ocurred trying to create a new cargo.'}, 500
        return cargo.json()

    def delete(self, nome):
        cargo = Cargo_Model.find_cargo(nome)
        if cargo:
            cargo.delete_cargo()
            return {'message':'cargo deleted.'}
        return {'message': 'cargo not found.'}, 404

class Cargo_By_Id(Resource):
    def get(self, cargo_id):
        cargo = Cargo_Model.find_by_id(cargo_id)
        if cargo: 
            return cargo.json()
        return {'message': 'cargo not found.'}, 404
