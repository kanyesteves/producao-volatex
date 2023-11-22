import sqlite3

conn = sqlite3.connect("db/db_producao.db")
c = conn.cursor()

# Querys
c.execute(
    "CREATE TABLE IF NOT EXISTS teares ([id] INTEGER PRIMARY KEY, [name] VARCHAR NOT NULL, [model] VARCHAR NOT NULL, [created_at] DATETIME)"
)
c.execute(
    "CREATE TABLE IF NOT EXISTS operators ([id] INTEGER PRIMARY KEY, [name] VARCHAR NOT NULL, [office] VARCHAR NOT NULL, [created_at] DATETIME)"
)
c.execute(
    "CREATE TABLE IF NOT EXISTS products_suppliers ([id] INTEGER PRIMARY KEY, [supplier] VARCHAR NOT NULL, [produto] VARCHAR NOT NULL, [created_at] DATETIME)"
)
c.execute(
    "CREATE TABLE IF NOT EXISTS production ([id] INTEGER PRIMARY KEY, [peso] FLOAT NOT NULL, [operador] VARCHAR NOT NULL, [cliente/produto] VARCHAR NOT NULL, [revisao] VARCHAR, [date] DATETIME)"
)