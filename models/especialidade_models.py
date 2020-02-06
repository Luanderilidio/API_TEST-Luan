from sql_alchemy import banco

class Especialidade_Model(banco.Model):
    __tablename__ = 'especialidades'

    especi_id = banco.Column(banco.Integer, primary_key=True)
    especialide = banco.Column(banco.String(80))
    funcionarios = banco.relationship('Funcionario_Model')

    def __init__(self,especialide):
        self.especialide = especialide


    def json(self):
        return {
            'especi_id': self.especi_id,
            'especialidade': self.especialide,
            'funcionarios': [funcionario.json() for funcionario in self.funcionarios]
        }

    @classmethod
    def find_especi(cls, especialide):
        especialidade = cls.query.filter_by(especialide=especialide).first()
        if especialidade:
            return especialidade
        return None

    @classmethod
    def find_by_id(cls, especi_id):
        especialidade = cls.query.filter_by(especi_id=especi_id).first()
        if especialidade:
            return especialidade.json()
        return None
        
    def save_especi(self):
        banco.session.add(self)
        banco.session.commit()

    def update_especi(self, especialidade):
        self.especialide = especialidade

    def delete_especi(self):
        banco.session.delete(self)
        banco.session.commit()
