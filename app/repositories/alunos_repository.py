import sqlite3
from db import get_connection
from app.models.alunos_model import Aluno

class AlunoRepository:

    # método criar aluno
    def create(self, aluno):
        try:
            with get_connection() as conn:
                conn.execute(
                    """
                    INSERT INTO alunos 
                    (cpf, nome, email, telefone, situacao, turma_id, curso_id, instituicao_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (aluno.cpf, aluno.nome, aluno.email, aluno.telefone, aluno.situacao,
                    aluno.turma_id, aluno.curso_id, aluno.instituicao_id)
                )
                conn.commit()
                return {"status": "ok", "message": "Aluno criado com sucesso!"}
        except sqlite3.IntegrityError as e:
            error_msg = str(e)
            print(f"[DEBUG]: {error_msg}")

            if "alunos.cpf" in error_msg:
                return {"status": "error", "message": "Erro: já existe um aluno com este CPF."}
            elif "alunos.email" in error_msg:
                return {"status": "error", "message": "Erro: já existe um aluno com este e-mail."}
            elif "alunos.telefone" in error_msg:
                return {"status": "error", "message": "Erro: já existe um aluno com este telefone."}
            else:
                return {"status": "error", "message": "Erro de unicidade em um campo único."}
        except Exception as e:
            # Para outros erros inesperados
            print(f"[DEBUG]: {e}")
            return {"status": "error", "message": f"Erro ao criar aluno: {e}"}


    # método listar todos os alunos
    def list_all(self):
        alunos = []
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT a.*, c.nome_curso, i.razao_social
                FROM alunos a
                JOIN cursos c ON a.curso_id = c.id
                JOIN instituicoes i ON a.instituicao_id = i.id
                """
            )
            for row in cursor.fetchall():
                alunos.append(
                    Aluno(
                        cpf=row["cpf"],
                        nome=row["nome"],
                        email=row["email"],
                        telefone=row["telefone"],
                        situacao=row["situacao"],
                        turma_id=row["turma_id"],
                        curso_id=row["curso_id"],
                        instituicao_id=row["instituicao_id"],
                        nome_curso=row["nome_curso"],
                        razao_social=row["razao_social"]
                    )
                )
        return alunos

    # método obter um aluno pelo CPF
    def get_by_cpf(self, cpf):
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM alunos WHERE cpf = ?", (cpf,)
            )
            row = cursor.fetchone()
            if row:
                return Aluno(
                    cpf=row["cpf"],
                    nome=row["nome"],
                    email=row["email"],
                    telefone=row["telefone"],
                    situacao=row["situacao"],
                    turma_id=row["turma_id"],
                    curso_id=row["curso_id"],
                    instituicao_id=row["instituicao_id"]
                )
            return None

    # método atualizar aluno
    def update(self, aluno):
        with get_connection() as conn:
            conn.execute(
                """
                UPDATE alunos
                SET nome = ?, email = ?, telefone = ?, situacao = ?, turma_id = ?, curso_id = ?, instituicao_id = ?
                WHERE cpf = ?
                """,
                (aluno.nome, aluno.email, aluno.telefone, aluno.situacao,
                 aluno.turma_id, aluno.curso_id, aluno.instituicao_id, aluno.cpf)
            )
            conn.commit()

    # método deletar aluno
    def delete(self, cpf):
        with get_connection() as conn:
            conn.execute(
                "DELETE FROM alunos WHERE cpf = ?", (cpf,)
            )
            conn.commit()
