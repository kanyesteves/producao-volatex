import requests, json
import pandas as pd
from datetime import datetime

class Services:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self.url = "http://127.0.0.1:8000"

    def event_data(self, event):
        dados = event.data
        return dados

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
        response = requests.get("http://localhost:8000/register/get_production/")
        try:
            response.raise_for_status()
            return response.text
        except requests.exceptions.HTTPError as http_err:
            print(f'Erro HTTP: {http_err}')


        query = "SELECT id, numero_peça, tear, peso, fornecedor, produto, revisao, operador, data FROM production"
        df = pd.read_sql(query, con=self.conn)
        return df

    def save(self, num_peca, peso, tear, operator, supplier, product, check):
        date_now = datetime.now()
        register_data = {
            "numero_peça": num_peca,
            "peso": peso,
            "tear": tear,
            "operador": operator,
            "fornecedor": supplier,
            "produto": product,
            "revisao": check,
            "data": date_now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        }
        url_save = self.url + "/register/save_production"
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(url_save, data=json.dumps(register_data), headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f'Erro HTTP: {http_err}')
