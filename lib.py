import requests, json
import pandas as pd
from datetime import datetime

class Services:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def get_operator(self):
        try:
            response = requests.get("http://192.168.1.5:8000/register/get_operators/")
            data = response.json()
            data_list = list(data.values())
            df = pd.DataFrame(data_list)
            return df
        except requests.exceptions.HTTPError as http_err:
            print(f'Erro HTTP: {http_err}')

    def get_tear(self):
        try:
            response = requests.get("http://192.168.1.5:8000/register/get_tear/")
            data = response.json()
            data_list = list(data.values())
            df = pd.DataFrame(data_list)
            return df
        except requests.exceptions.HTTPError as http_err:
            print(f'Erro HTTP: {http_err}')

    def get_products_supplier(self):
        try:
            response = requests.get("http://192.168.1.5:8000/register/get_products_suppliers/")
            data = response.json()
            data_list = list(data.values())
            df = pd.DataFrame(data_list)
            return df
        except requests.exceptions.HTTPError as http_err:
            print(f'Erro HTTP: {http_err}')

    def get_production(self):
        try:
            response = requests.get("http://192.168.1.5:8000/register/get_production/")
            data = response.json()
            data_list = list(data.values())
            df = pd.DataFrame(data_list)
            return df
        except requests.exceptions.HTTPError as http_err:
            print(f'Erro HTTP: {http_err}')

    def save_production(self, num_peca, peso, tear, operator, supplier, product, check, remove):
        date_now = datetime.now()
        register_data = {
            "num_peça": num_peca,
            "peso": peso,
            "tear": tear,
            "operador": operator,
            "fornecedor": supplier,
            "produto": product,
            "revisao": check,
            "remove": remove,
            "data": date_now.strftime("%Y-%m-%d")
        }
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post("http://192.168.1.5:8000/register/save_production", data=json.dumps(register_data), headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as http_err:
            print(f'Erro HTTP: {http_err}')

    def save_tear(self, name_tear, model_tear, remove):
        date_now = datetime.now()
        register_data = {
            "nome": name_tear,
            "modelo": model_tear,
            "remove": remove,
            "data": date_now.strftime("%Y-%m-%d")
        }
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post("http://192.168.1.5:8000/config/save_tear", data=json.dumps(register_data), headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as http_err:
            print(f'Erro HTTP: {http_err}')

    def save_operator(self, name_operator, office_operator, remove):
        date_now = datetime.now()
        register_data = {
            "nome": name_operator,
            "cargo": office_operator,
            "remove": remove,
            "data": date_now.strftime("%Y-%m-%d")
        }
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post("http://192.168.1.5:8000/config/save_operator", data=json.dumps(register_data), headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as http_err:
            print(f'Erro HTTP: {http_err}')

    def save_product_supplier(self, supplier, product, remove):
        date_now = datetime.now()
        register_data = {
            "fornecedor": supplier,
            "produto": product,
            "remove": remove,
            "data": date_now.strftime("%Y-%m-%d")
        }
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post("http://192.168.1.5:8000/config/save_products_supplier", data=json.dumps(register_data), headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as http_err:
            print(f'Erro HTTP: {http_err}')
