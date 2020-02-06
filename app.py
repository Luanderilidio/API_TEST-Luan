from flask import Flask, jsonify
from flask_restful import Api
from dynaconf import FlaskDynaconf
from resources.cargo_resources import Cargo_all, Cargo_Specific, Cargo_By_Id
from resources.funcionario_resources import Funcionarios_all, Funcionarios_Specific
from resources.especialidades_resources import Especialidade_all, Especialide_Specific

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRAC_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()


api.add_resource(Cargo_all, '/cargos')
api.add_resource(Cargo_Specific, '/cargos/<string:nome>')
api.add_resource(Funcionarios_all, '/funcionarios')
api.add_resource(Funcionarios_Specific, '/funcionarios/<int:func_id>')
api.add_resource(Cargo_By_Id, '/cargo_by_id/<int:cargo_id>')
api.add_resource(Especialidade_all, '/especialidades')
api.add_resource(Especialide_Specific, '/especialidades/<string:especialidade>')


if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
