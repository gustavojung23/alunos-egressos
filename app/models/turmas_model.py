class Turma:
    def __init__(self, id, nome_turma, curso_id, instituicao_id):
        self.id = id
        self.nome_turma = nome_turma
        self.curso_id = curso_id
        self.instituicao_id = instituicao_id

    def __repr__(self):
        return f"<Turma {self.id} - {self.nome_turma}"