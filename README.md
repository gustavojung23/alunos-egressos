# 💻 Sistema de Alunos Egressos

Sistema web para gerenciamento de alunos que não fazem mais parte das instituições cadastradas.
Nesta versão inicial, é possível cadastrar, editar, gerenciar e deletar:

- 🏫 Instituições
- 🎓 Cursos
- 🧑‍🏫 Turmas
- 🧑‍🎓 Alunos


## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/stable/)
- [Sqlite3](https://sqlite.org/)
- [Bootstrap](https://getbootstrap.com/)


## ⚙️ Como utilizar
### 1. Clonar o repositório
```bash
git clone https://github.com/gustavojung23/alunos-egressos.git
cd sistema-alunos-egressos
```

### 2. Criar ambiente virtual Python
- Windows:
```bash
python -m venv venv
```

- Linux\macOS:
```bash
python3 -m venv venv
```

### 3. Ativar ambiente virtual
- Windows:
```bash
venv\Scripts\activate
```

- Linux\macOS:
```bash
source venv/bin/activate
```

### 4. Instalar dependências
```bash
pip install -r requirements.txt
```

### 5. Declare as variáveis de ambiente
- Em seu projeto crie o arquivo .env e declare as variáveis de ambiente conforme abaixo.
```bash
DB_NAME="" #nome do banco (string)
SECRET_KEY="" #chave secreta para uso do flash() (string).
```

### 6. Execute o Banco de Dados
```bash
python init_db.py
```

### 7. Executar a aplicação
```bash
python app.py
```

Acesse no navegador:
http://localhost:5000