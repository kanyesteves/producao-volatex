import sqlite3

conn = sqlite3.connect("db/db_producao.db")
c = conn.cursor()

# Querys
# c.execute(
#     "DROP TABLE production"
# )
c.execute(
    "CREATE TABLE production ([id] INTEGER PRIMARY KEY, [num_peca] INTEGER NOT NULL, [tear] VARCHAR NOT NULL, [peso] FLOAT NOT NULL, [product_supplier] VARCHAR NOT NULL, [check_production] VARCHAR NOT NULL, [operator] VARCHAR NOT NULL, [data] DATETIME)"
)