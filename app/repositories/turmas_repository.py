import sqlite3
from db import get_connection
from app.models.turmas_model import Turma

class TurmasRepository:

    #método para criar curso.
    def create(self, turma):
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO turmas (nome_turma, curso_id, instituicao_id) VALUES (?, ?, ?)",
                (turma.nome_turma, turma.curso_id, turma.instituicao_id)
            )
            conn.commit()


    # método para listar as turmas e respectivos cursos/instituições
    def list_turmas(self):
        turmas = []
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
                SELECT turmas.id, turmas.nome_turma, turmas.curso_id, turmas.instituicao_id, cursos.nome_curso
                FROM turmas
                JOIN cursos ON turmas.curso_id = cursos.id
            ''')
            rows = cursor.fetchall()
            for row in rows:
                turma = Turma(
                    id=row["id"],
                    nome_turma=row["nome_turma"],
                    curso_id=row["curso_id"],
                    instituicao_id=row["instituicao_id"],
                    nome_curso=row["nome_curso"]
                )
                turmas.append(turma)

        return turmas
        

    # método retorna uma turma
    def get_by_id_turma(self, id):
        with get_connection() as conn:
            row = conn.execute(
                '''
                    SELECT turmas.id, turmas.nome_turma, turmas.curso_id, turmas.instituicao_id, cursos.nome_curso, instituicoes.razao_social
                    FROM turmas
                    JOIN cursos ON turmas.curso_id = cursos.id
                    JOIN instituicoes ON turmas.instituicao_id = instituicoes.id
                    WHERE turmas.id = ?
                ''', (id,)).fetchone()
            if row:
                return Turma(
                    id=row['id'],
                    nome_turma=row['nome_turma'],
                    curso_id=row['curso_id'],
                    instituicao_id=row['instituicao_id'],
                    nome_curso=row['nome_curso'],
                    razao_social=row['razao_social']
                )
            return None
        

    # método para atualizar uma turma
    def update(self, turma):
        with get_connection() as conn:
            conn.execute(
                "UPDATE turmas SET nome_turma = ?, curso_id = ?, instituicao_id = ? WHERE id = ?",
                (turma.nome_turma, turma.curso_id, turma.instituicao_id, turma.id)
            )
            conn.commit()


    # método para apagar uma turma
    def delete(self, id):
        with get_connection() as conn:
            conn.execute(
                'DELETE FROM turmas WHERE id = ?', (id,)
            )
            conn.commit()