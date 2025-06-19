# Classe Institution
class Institution:
    def __init__(self, id=None, nome=None, razao_social=None):
        self.id = id
        self.nome = nome
        self.razao_social = razao_social

    def __repr__(self):
        return f"<Instituicao {self.id} - {self.nome} ({self.razao_social})>"