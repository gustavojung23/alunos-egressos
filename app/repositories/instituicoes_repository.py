import sqlite3
from db import get_connection
from app.models.instituicoes_model import Institution

## classe para executar as querys que vão para o banco
class InstitutionRepository:

    ## metódo para criar o dado no banco.
    def create(self, instituicao):
        with get_connection() as conn:
            conn.execute(
                'INSERT INTO instituicoes (nome, razao_social) VALUES (?, ?)',
                (instituicao.nome, instituicao.razao_social)
            )
            conn.commit()

    ## método para listar as instituições.
    def list_institutions(self):
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM instituicoes')
            rows = cursor.fetchall()
            return [Institution(row['id'], row['nome'], row['razao_social']) for row in rows]