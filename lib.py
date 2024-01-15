import pandas as pd

class Functions:
    def __init__(self, conn):
        self.conn = conn

    def get_operator(self):
        query = "SELECT id, name, office, created_at FROM operators"
        df = pd.read_sql(query, con=self.conn)
        return df

    def get_tear(self):
        query = "SELECT id, name, model, created_at FROM teares"
        df = pd.read_sql(query, con=self.conn)
        return df

    def get_products_supplier(self):
        query = "SELECT id, supplier, produto, created_at FROM products_suppliers"
        df = pd.read_sql(query, con=self.conn)
        return df

    def get_production(self):
        query = "SELECT id, num_peca, tear, peso, supplier, product, check_production, operator, data FROM production"
        df = pd.read_sql(query, con=self.conn)
        return df