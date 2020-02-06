from sql_alchemy import banco

class Funcionario_Model(banco.Model):
    __tablename__ = 'funcionarios'

    func_id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(80))
    idade = banco.Column(banco.String(20))
    cargo_id = banco.Column(banco.Integer, banco.ForeignKey('cargos.cargo_id'))
    especi_id = banco.Column(banco.Integer, banco.ForeignKey('especialidades.especi_id'))


    def __init__(self, func_id, nome, idade, cargo_id, especi_id):
        self.func_id = func_id
        self.nome = nome
        self.idade = idade
        self.cargo_id = cargo_id
        self.especi_id = especi_id

    def json(self):
        return {
            'func_id': self.func_id,
            'nome': self.nome,
            'idade': self.idade,
            'cargo_id': self.cargo_id,
            'especi_id': self.especi_id
        }

    @classmethod
    def find_func(cls, func_id):
        funcionario = cls.query.filter_by(func_id=func_id).first()
        if funcionario:
            return funcionario
        return None

    def save_func(self):
        banco.session.add(self)
        banco.session.commit()

    def update_func(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def delete_func(self):
        banco.session.delete(self)
        banco.session.commit()
