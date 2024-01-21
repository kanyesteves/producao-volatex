import sqlite3
import pandas as pd

conn = sqlite3.connect("db/db_producao.db")
c = conn.cursor()

# Querys
c.execute(
    "ALTER TABLE operators RENAME office to cargo"
    # "CREATE TABLE production ([id] INTEGER PRIMARY KEY, [num_peca] VARCHAR NOT NULL, [tear] VARCHAR NOT NULL, [peso] FLOAT NOT NULL, [supplier] VARCHAR NOT NULL, [product] VARCHAR NOT NULL, [check_production] VARCHAR NOT NULL, [operator] VARCHAR NOT NULL, [data] DATETIME)"
    # "DELETE FROM production"
    # "DELETE FROM teares"
    # "INSERT INTO users (username, password, user_type) VALUES (?, ?, ?)", ('admin', 'x1y2z3adminVol@tex', 'admin')
    # "INSERT INTO users (username, password, user_type) VALUES (?, ?, ?)", ('producao', 'z3y2x1prodVol@tex', 'operador')
    # "CREATE TABLE users ([id] INTEGER PRIMARY KEY AUTOINCREMENT, [username] TEXT NOT NULL UNIQUE, [password] TEXT NOT NULL, [user_type] TEXT NOT NULL)"
)
conn.commit()