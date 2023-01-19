import sqlite3

conn = sqlite3.connect("bancodedados.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    Senha TEXT NOT NULL,
    Estado TEXT NOT NULL,
    Profissao TEXT NOT NULL
);
""")