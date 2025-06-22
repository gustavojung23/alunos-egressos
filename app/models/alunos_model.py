class Aluno:
    def __init__(self, cpf, nome, email, situacao, turma_id, curso_id, instituicao_id, telefone=None, nome_curso=None, razao_social=None):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.situacao = situacao
        self.turma_id = turma_id
        self.curso_id = curso_id
        self.instituicao_id = instituicao_id
        self.nome_curso = nome_curso
        self.razao_social = razao_social

    def __repr__(self):
        return f"<Aluno {self.cpf} - {self.nome}"