from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.instituicoes_model import Institution
from app.repositories.instituicoes_repository import InstitutionRepository

# Encapsulamento de rotas - Instituição
institution_bp = Blueprint('instituicao', __name__, url_prefix='/instituicoes')
repo = InstitutionRepository()

@institution_bp.route('/')
def index():
    institutions = repo.list_institutions()
    return render_template('instituicoes/index.html', institutions=institutions)

# Rota para criar uma nova instituição
@institution_bp.route('/cadastrar', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        nome = request.form["nome"]
        razao_social = request.form["razao_social"]

        # Validação de preenchimento de dados.
        if not nome or not razao_social:
            flash("Preencha todos os campos", "error")
            return redirect(url_for("instituicao.create"))
        
        institution_new = Institution(nome=nome, razao_social=razao_social)
        repo.create(institution_new)
        flash("Instituição criada com sucesso!", "success")
        return redirect(url_for('instituicao.index'))
    
    return render_template("instituicoes/create.html")


# Rota que retorna uma instituição para edição.
@institution_bp.route('/editar/<int:id>', methods=["GET", "POST"])
def update(id):
    get_by_id = repo.get_by_id_institution(id)
    if request.method == "POST":
        nome = request.form["nome"]
        razao_social = request.form["razao_social"]

         # Validação de preenchimento de dados.
        if not nome or not razao_social:
            flash("Preencha todos os campos", "error")
            return redirect(url_for("instituicao.create"))
        
        institution_update = Institution(id=id, nome=nome, razao_social=razao_social)
        repo.update(institution_update)
        flash("Instituição atualizada com sucesso!", "success")
        return redirect(url_for('instituicao.index'))
    
    return render_template("instituicoes/editar.html", instituicao=get_by_id)

# Rota para deletar instituição.
@institution_bp.route('/deletar/<int:id>', methods=["POST"])
def delete(id):
    repo.delete(id)
    flash("Instituição deletada com sucesso", "success")
    return redirect(url_for("instituicao.index"))