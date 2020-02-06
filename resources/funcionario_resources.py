from flask_restful import Resource, reqparse
from models.funcionario_models import Funcionario_Model
from models.cargo_models import Cargo_Model


class Funcionarios_all(Resource):
    def get(self):
        return {'funcionarios': [funcionario.json() for funcionario in Funcionario_Model.query.all()]} # SELECT * FROM hoteis

class Funcionarios_Specific(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank.")
    atributos.add_argument('idade', type=str, required=True, help="The field 'idade' cannot be left blank.")
    atributos.add_argument('cargo_id', type=int, required=True, help="Every 'cargo_id' needs to be linked with a cargo.")
    atributos.add_argument('especi_id', type=int, required=True, help="Every 'especi_id' needs to be linked with a cargo.")


    def get(self, func_id):
        funcionario = Funcionario_Model.find_func(func_id)
        if funcionario:
            return funcionario.json()
        return {'message': 'funcionario not found.'}, 404

    def post(self, func_id):
        if Funcionario_Model.find_func(func_id):
            return {"message": "Func_id '{}' already exists.".format(func_id)}, 400 #Bad Request

        dados = Funcionarios_Specific.atributos.parse_args()
        funcionario = Funcionario_Model(func_id, **dados)

        if not Cargo_Model.find_by_id(dados['cargo_id']):
            return {'message': 'The cargo must be associated to a valid cargo_id.'}, 400

        try:
            funcionario.save_func()
        except:
            return {"message": "An error ocurred trying to create funcionario."}, 500 #Internal Server Error
        return funcionario.json(), 201

    def put(self, func_id):
        dados = Funcionarios_Specific.atributos.parse_args()
        funcionario = Funcionario_Model(func_id, **dados)

        funcionario_encontrado = Funcionario_Model.find_func(func_id)
        if funcionario_encontrado:
            funcionario_encontrado.update_func(**dados)
            funcionario_encontrado.save_func()
            return funcionario_encontrado.json(), 200
        funcionario_encontrado.save_func()
        return funcionario.json(), 201

    def delete(self, func_id):
        funcionario = Funcionario_Model.find_func(func_id)
        if funcionario:
            funcionario.delete_func()
            return {'message': 'Funcionario deleted.'}
        return {'message': 'Funcionario not found.'}, 404
