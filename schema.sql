--SQL para criação das tabelas
/*
DROP TABLE cursos;
*/

CREATE TABLE IF NOT EXISTS instituicoes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(150) NOT NULL,
    razao_social VARCHAR(150) NOT NULL
);

CREATE TABLE IF NOT EXISTS cursos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_curso VARCHAR(150) NOT NULL,
    id_instituicao INTEGER NOT NULL,
    FOREIGN KEY (id_instituicao) REFERENCES instituicoes(id) ON DELETE CASCADE
);