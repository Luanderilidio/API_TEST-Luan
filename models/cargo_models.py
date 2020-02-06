from sql_alchemy import banco

class Cargo_Model(banco.Model):
    __tablename__ = 'cargos'

    cargo_id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(80))
    salario = banco.Column(banco.Float(precision=2))
    funcionarios = banco.relationship('Funcionario_Model')

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def json(self):
        return {
            'cargo_id': self.cargo_id,
            'nome': self.nome,
            'salario': self.salario,
            'funcionarios': [funcionario.json() for funcionario in self.funcionarios]
        }

    @classmethod
    def find_cargo(cls, nome):
        cargo = cls.query.filter_by(nome=nome).first()
        if cargo:
            return cargo
        return None

    @classmethod
    def find_by_id(cls, cargo_id):
        cargo = cls.query.filter_by(cargo_id=cargo_id).first()
        if cargo:
            return cargo
        return None

    def save_cargo(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_cargo(self):
        banco.session.delete(self)
        banco.session.commit()
