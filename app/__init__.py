import os
from db import get_connection
from flask import Flask, render_template
from app.controllers.instituicoes_controller import institution_bp


def create_app():
    app = Flask(__name__, template_folder='views')
    app.secret_key = os.getenv('SECRET_KEY')
    app.config['DATABASE'] = 'app.db'

    with get_connection() as conn:
        conn.execute('PRAGMA journal_mode=WAL;')

    app.register_blueprint(institution_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app