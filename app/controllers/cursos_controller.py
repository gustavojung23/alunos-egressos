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

# controller para criação do curso.
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
    
    #lista de instituições cadastradas para serem selecionadas junto ao curso.
    instituicoes = repoInstitution.list_institutions()
    return render_template("cursos/create.html", instituicoes=instituicoes)

#Rota para atualizar curso
@curso_bp.route('/atualizar/curso/<int:id>', methods=["GET", "POST"])
def update(id):
    if request.method == 'POST':
        nome_curso = request.form['nome_curso']
        razao_social_instituicao = request.form['razao_social_instituicao']

        # Buscar a instituição pelo razao_social
        instituicao = repoInstitution.get_by_razao_social_institution(razao_social_instituicao)
        if not instituicao:
            flash('Instituição não encontrada!', 'error')
            return redirect(url_for('curso.update', id=id))

        # Atualizar o curso
        curso = Curso(id=id, nome_curso=nome_curso, id_instituicao=int(instituicao.id))
        repo.update(curso)

        flash('Curso atualizado com sucesso!', 'success')
        return redirect(url_for('curso.index'))

    # método GET: buscar o curso e as instituicoes para o select
    curso = repo.buscar_curso(id)
    instituicoes = repoInstitution.list_institutions()
    return render_template('cursos/editar.html', curso=curso, instituicoes=instituicoes)

# Rota para listar um curso.
@curso_bp.route('curso/<int:id>', methods=["GET"])
def buscar_curso(id):
    curso = repo.buscar_curso(id)
    return render_template("cursos/curso.html", curso=curso)

# Rota para deletar curso.
@curso_bp.route('/deletar/<int:id>', methods=["POST"])
def delete(id):
    repo.delete(id)
    flash("Curso deletado com sucesso", "success")
    return redirect(url_for("curso.index"))