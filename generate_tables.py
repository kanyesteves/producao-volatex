import sqlite3

conn = sqlite3.connect("db/db_producao.db")
c = conn.cursor()

# Querys
c.execute(
    "CREATE TABLE IF NOT EXISTS tear_1 ([id] INTEGER PRIMARY KEY, [peso] FLOAT NOT NULL, [operador] VARCHAR NOT NULL, [cliente/produto] VARCHAR NOT NULL, [revisao] VARCHAR, [data] DATETIME)"
)
c.execute(
    "CREATE TABLE IF NOT EXISTS tear_2 ([id] INTEGER PRIMARY KEY, [peso] FLOAT NOT NULL, [operador] VARCHAR NOT NULL, [cliente/produto] VARCHAR NOT NULL, [revisao] VARCHAR, [data] DATETIME)"
)
c.execute(
    "CREATE TABLE IF NOT EXISTS tear_3 ([id] INTEGER PRIMARY KEY, [peso] FLOAT NOT NULL, [operador] VARCHAR NOT NULL, [cliente/produto] VARCHAR NOT NULL, [revisao] VARCHAR, [data] DATETIME)"
)
c.execute(
    "CREATE TABLE IF NOT EXISTS tear_3 ([id] INTEGER PRIMARY KEY, [peso] FLOAT NOT NULL, [operador] VARCHAR NOT NULL, [cliente/produto] VARCHAR NOT NULL, [revisao] VARCHAR, [data] DATETIME)"
)
