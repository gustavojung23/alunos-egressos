from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.alunos_model import Aluno
from app.repositories.alunos_repository import AlunoRepository
from app.repositories.cursos_repository import CursosRepository
from app.repositories.turmas_repository import TurmasRepository
from app.repositories.instituicoes_repository import InstitutionRepository

aluno_bp = Blueprint('aluno', __name__, url_prefix='/alunos')
repo = AlunoRepository()
repo_curso = CursosRepository()
repo_turma = TurmasRepository()
repo_inst = InstitutionRepository()

@aluno_bp.route('/')
def index():
    alunos = repo.list_all()
    return render_template('alunos/index.html', alunos=alunos)

@aluno_bp.route('/cadastrar', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        aluno = Aluno(
            cpf=request.form['cpf'],
            nome=request.form['nome'],
            email=request.form['email'],
            telefone=request.form['telefone'],
            situacao=request.form['situacao'],
            turma_id=int(request.form['turma_id']),
            curso_id=int(request.form['curso_id']),
            instituicao_id=int(request.form['instituicao_id'])
        )

        resultado = repo.create(aluno)
        if resultado["status"] == "ok":
            flash(resultado["message"], 'success')
        else:
            flash(resultado["message"], 'danger')

        return redirect(url_for('aluno.index'))
    instituicoes = repo_inst.list_institutions()
    cursos = repo_curso.list_cursos()
    turmas = repo_turma.list_turmas()
    return render_template('alunos/create.html',instituicoes=instituicoes, cursos=cursos, turmas=turmas)

@aluno_bp.route('/editar/<cpf>', methods=['GET', 'POST'])
def update(cpf):
    aluno = repo.get_by_cpf(cpf)
    if not aluno:
        flash('Aluno não encontrado!', 'error')
        return redirect(url_for('aluno.index'))
    if request.method == 'POST':
        aluno.nome = request.form['nome']
        aluno.email = request.form['email']
        aluno.telefone = request.form['telefone']
        aluno.situacao = request.form['situacao']
        aluno.turma_id = int(request.form['turma_id'])
        aluno.curso_id = int(request.form['curso_id'])
        aluno.instituicao_id = int(request.form['instituicao_id'])

        repo.update(aluno)
        flash('Aluno atualizado com sucesso!', 'success')
        return redirect(url_for('aluno.index'))

    instituicoes = repo_inst.list_institutions()
    cursos = repo_curso.list_cursos()
    turmas = repo_turma.list_turmas()
    return render_template('alunos/edit.html', aluno=aluno, instituicoes=instituicoes, cursos=cursos, turmas=turmas)

@aluno_bp.route('/deletar/<cpf>', methods=['POST'])
def delete(cpf):
    repo.delete(cpf)
    flash('Aluno deletado com sucesso!', 'success')
    return redirect(url_for('aluno.index'))
