import sqlite3

#lê o banco de dados, se não existir ele cria.
with open("schema.sql", "r", encoding="utf-8") as f:
    sql_script = f.read()

conn = sqlite3.connect("app.db")
conn.executescript(sql_script)
conn.commit()
conn.close()

print("Banco de Dados Criado")