import sqlite3
from db import get_connection
from app.models.instituicoes_model import Institution

## classe para executar as querys que vão para o banco
class InstitutionRepository:

    ## metódo para criar uma instituição.
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
    
    ## método atualizar instituição.
    def update(self, instituicao):
        with get_connection() as conn:
            conn.execute(
                'UPDATE instituicoes SET nome = ?, razao_social = ? WHERE id = ?',
                (instituicao.nome, instituicao.razao_social, instituicao.id)
            )
            conn.commit()

    ## método retorna apenas uma instituição.
    def get_by_id_institution(self, id):
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM instituicoes WHERE id = ?', (id,)
            )
            row = cursor.fetchone()
            if row:
                return Institution(id=row["id"], nome=row["nome"], razao_social=row["razao_social"])
            return None
        
    ## método deletar dado do banco.
    def delete(self, id):
        with get_connection() as conn:
            conn.execute(
                'DELETE FROM instituicoes WHERE id = ?', (id,)
            )
            conn.commit()

    def get_by_razao_social_institution(self, razao_social):
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                'SELECT id, nome, razao_social FROM instituicoes WHERE razao_social = ?',
                (razao_social,)
            )
            row = cursor.fetchone()
            return Institution(row['id'], row['nome'], row['razao_social']) if row else None
