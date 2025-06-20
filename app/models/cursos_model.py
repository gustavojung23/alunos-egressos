# Classe Curso
class Curso:
    def __init__(self, id, nome_curso, id_instituicao, razao_social_instituicao=None):
        self.id = id
        self.nome_curso = nome_curso
        self.id_instituicao = id_instituicao
        self.razao_social_instituicao = razao_social_instituicao

    def __repr__(self):
        return f"<Curso {self.id} - {self.nome_curso} ({self.razao_social_instituicao or self.id_instituicao})>"