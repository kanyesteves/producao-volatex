import sqlite3
import pandas as pd

conn = sqlite3.connect("db/db_producao.db")
c = conn.cursor()

# Querys
c.execute(
    # "CREATE TABLE production ([id] INTEGER PRIMARY KEY, [num_peca] VARCHAR NOT NULL, [tear] VARCHAR NOT NULL, [peso] FLOAT NOT NULL, [supplier] VARCHAR NOT NULL, [product] VARCHAR NOT NULL, [check_production] VARCHAR NOT NULL, [operator] VARCHAR NOT NULL, [data] DATETIME)"
    # "DROP TABLE production"
    "INSERT INTO users (username, password, user_type) VALUES (?, ?, ?)", ('kany', '132567', 'admin')
    # "CREATE TABLE users ([id] INTEGER PRIMARY KEY AUTOINCREMENT, [username] TEXT NOT NULL UNIQUE, [password] TEXT NOT NULL, [user_type] TEXT NOT NULL)"
)
conn.commit()