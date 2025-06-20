import os
from dotenv import load_dotenv
from db import get_connection
from flask import Flask, render_template
from app.controllers.instituicoes_controller import institution_bp
from app.controllers.cursos_controller import curso_bp

load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='views')
    app.secret_key = os.getenv('SECRET_KEY')
    app.config['DATABASE'] = os.path.join(os.path.dirname(__file__), 'app.db')

    with get_connection() as conn:
        conn.execute('PRAGMA journal_mode=WAL;')
        conn.execute('PRAGMA foreign_keys = ON')

    app.register_blueprint(institution_bp)
    app.register_blueprint(curso_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app