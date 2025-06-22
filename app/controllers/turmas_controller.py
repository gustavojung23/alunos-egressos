from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.turmas_model import Turma
from app.repositories.turmas_repository import TurmasRepository
from app.repositories.instituicoes_repository import InstitutionRepository
from app.repositories.cursos_repository import CursosRepository

# Encapsulamento de rotas - Turmas
turma_bp = Blueprint("turma", __name__, url_prefix="/turmas")

# instância classe
repo = TurmasRepository()
repoInstitution = InstitutionRepository()
repoCursos = CursosRepository()

# Rota inicial para listar todas as turmas cadastradas.
@turma_bp.route("/")
def index():
    turmas = repo.list_turmas()
    return render_template("turmas/index.html", turmas=turmas)


# Rota para retornar uma turma.
@turma_bp.route("/turma/<int:id>", methods=["GET"])
def show(id):
    turma = repo.get_by_id_turma(id)
    return render_template("turmas/turma.html", turma=turma)


# Rota para cadastro de Turmas.
@turma_bp.route("/cadastrar", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        nome_turma = request.form["nome_turma"]
        curso_id = int(request.form["curso_id"])
        instituicao_id = int(request.form["instituicao_id"])

        if not nome_turma or not curso_id or not instituicao_id:
            flash("Todos os campos devem ser preenchidos", "error")

        turma = Turma(id=None, nome_turma=nome_turma, curso_id=curso_id, instituicao_id=instituicao_id)
        print(type(turma.nome_turma), turma.nome_turma)
        print(type(turma.curso_id), turma.curso_id)
        print(type(turma.instituicao_id), turma.instituicao_id)
        repo.create(turma)
        flash("Turma Cadastrada", "success")
        
        return redirect(url_for("turma.index"))
    
    #lista de instituições cadastradas para serem selecionadas junto ao curso.
    instituicoes = repoInstitution.list_institutions()
    cursos = repoCursos.list_cursos()
    return render_template("turmas/create.html", instituicoes=instituicoes, cursos=cursos)

# Rota para atualizar a Turma.
@turma_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def update(id):
    turma = repo.get_by_id_turma(id)

    # Faz validação se existe a turma
    if not turma:
        flash("Turma não encontrada", "error")
        return redirect(url_for("turma.index"))

    if request.method == "POST":
        nome_turma = request.form["nome_turma"]
        curso_id = int(request.form["curso_id"])
        instituicao_id = int(request.form["instituicao_id"])

        # Obrigatório o preenchimento
        if not nome_turma or not curso_id or not instituicao_id:
            flash("Todos os campos devem ser preenchidos", "error")
            return render_template("turmas/editar.html",
                turma=turma,
                instituicoes=repoInstitution.list_institutions(),
                cursos=repoCursos.list_cursos(),
            )
        
        # Faz a atualização
        turma = Turma(id=id, nome_turma=nome_turma, curso_id=curso_id, instituicao_id=instituicao_id)
        print(type(turma.nome_turma), turma.nome_turma)
        print(type(turma.curso_id), turma.curso_id)
        print(type(turma.instituicao_id), turma.instituicao_id)
        repo.update(turma)

        flash("Turma Atualizada com sucesso", "success")
        return redirect(url_for("turma.index"))
    
    instituicoes = repoInstitution.list_institutions()
    cursos = repoCursos.list_cursos()
    return render_template(
        "turmas/editar.html",
        turma=turma,
        instituicoes=instituicoes,
        cursos=cursos
    )

# Rota para deletar curso.
@turma_bp.route('/deletar/<int:id>', methods=["POST"])
def delete(id):
    repo.delete(id)
    flash("Turma deletado com sucesso", "success")
    return redirect(url_for("turma.index"))