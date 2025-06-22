class Turma:
    def __init__(self, id, nome_turma, curso_id, instituicao_id, nome_curso=None, razao_social=None):
        self.id = id
        self.nome_turma = nome_turma
        self.curso_id = curso_id
        self.instituicao_id = instituicao_id
        self.nome_curso = nome_curso
        self.razao_social = razao_social

    def __repr__(self):
        return f"<Turma {self.id} - {self.nome_turma}"