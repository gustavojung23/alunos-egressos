from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.instituicoes_model import Institution
from repositories.instituicoes_repository import InstitutionRepository

# Encapsulamento de rotas - Instituição
institution_bp = Blueprint('instituicao', __name__, url_prefix='/instituicoes')
repo = InstitutionRepository()

@institution_bp.route('/')
def index():
    institutions = repo.list_institutions()
    return render_template('instituicoes/index.html', institutions=institutions)

# Rota para criar uma nova instituição
@institution_bp.route('/new', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        nome = request.form["nome"]
        razao_social = request.form["razao_social"]
        
        # Verifica se tem valor
        if nome and razao_social:
            # Chama o construtor da classe Institution
            new_institution = Institution(nome=nome, razao_social=razao_social)
            
            # Persiste no banco
            repo.create(new_institution)

            #mensagem flash em caso de sucesso
            flash('Instituição criada com sucesso')
        return redirect(url_for('instituicao.index'))
        
    return render_template('instituicoes/create.html')