--SQL para criação das tabelas

CREATE TABLE IF NOT EXISTS instituicoes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(150) NOT NULL,
    razao_social VARCHAR(150) NOT NULL
)