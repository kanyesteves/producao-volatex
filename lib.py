import pandas as pd

class Functions:
    def __init__(self, conn):
        self.conn = conn

    def get_operator(self):
        query = "SELECT id, nome, cargo, created_at FROM operators"
        df = pd.read_sql(query, con=self.conn)
        return df

    def get_tear(self):
        query = "SELECT id, nome, modelo, created_at FROM teares"
        df = pd.read_sql(query, con=self.conn)
        return df

    def get_products_supplier(self):
        query = "SELECT id, fornecedor, produto, created_at FROM products_suppliers"
        df = pd.read_sql(query, con=self.conn)
        return df

    def get_production(self):
        query = "SELECT id, numero_peça, tear, peso, fornecedor, produto, revisao, operador, data FROM production"
        df = pd.read_sql(query, con=self.conn)
        return df