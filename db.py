import sqlite3

#função que faz a conexão com o banco.
def get_connection():
    conn = sqlite3.connect("app.db", timeout=10)
    conn.row_factory = sqlite3.Row
    return conn