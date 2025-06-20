from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.cursos_model import Curso
from app.repositories.cursos_repository import CursosRepository
from app.repositories.instituicoes_repository import InstitutionRepository

# Encapsulamento de rotas - Cursos
curso_bp = Blueprint('curso', __name__, url_prefix='/cursos')

# instância classe
repo = CursosRepository()
repoInstitution = InstitutionRepository()

# página inicial de cursos - onde listam todos os cursos cadastrados ou nenhum.
@curso_bp.route('/')
def index():
    cursos = repo.list_cursos()
    return render_template('cursos/index.html', cursos=cursos)

@curso_bp.route('/cadastrar', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        nome_curso = request.form["nome_curso"]
        id_instituicao = request.form["id_instituicao"]

        # Validação de preenchimento de dados.
        if not nome_curso or not id_instituicao:
            flash("Preencha todos os campos", "error")
            return redirect(url_for("curso.create"))
        
        curse_new = Curso(id=None, nome_curso=nome_curso, id_instituicao=int(id_instituicao))
        repo.create(curse_new)
        flash("Curso criado com sucesso!", "success")
        return redirect(url_for('curso.index'))
    
    instituicoes = repoInstitution.list_institutions()
    return render_template("cursos/create.html", instituicoes=instituicoes)