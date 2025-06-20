import sqlite3
from db import get_connection
from app.models.cursos_model import Curso

class CursosRepository:

    #método para criar um curso.
    def create(self, curso):
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO cursos (nome_curso, id_instituicao) VALUES (?, ?)",
                (curso.nome_curso, curso.id_instituicao)
            )
            conn.commit()

    #método para retornar todos os cursos com a razão social da instituição.
    def list_cursos(self):
        cursos = []
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
                SELECT cursos.id, cursos.nome_curso, cursos.id_instituicao, instituicoes.razao_social
                FROM cursos
                JOIN instituicoes ON cursos.id_instituicao = instituicoes.id
            ''')
            rows = cursor.fetchall()
            for row in rows:
                curso = Curso(
                    id=row["id"],
                    nome_curso=row["nome_curso"],
                    id_instituicao=row["id_instituicao"],
                    razao_social_instituicao=row["razao_social"]
                )
                cursos.append(curso)

        return cursos