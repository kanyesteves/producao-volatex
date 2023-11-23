import pandas as pd
import streamlit as st
import sqlite3
from datetime import datetime


st.set_page_config(
    layout="wide",
    page_title="SysProduct-Volatex"
)


# Variáveis Globais
conn = sqlite3.connect("db/db_producao.db")
c = conn.cursor()


# Funções
def get_operator():
    query = "SELECT name, office, created_at FROM operators"
    df = pd.read_sql(query, con=conn)
    return df

def get_tear():
    query = "SELECT name, model, created_at FROM teares"
    df = pd.read_sql(query, con=conn)
    return df

def get_products_supplier():
    query = "SELECT supplier, produto, created_at FROM products_suppliers"
    df = pd.read_sql(query, con=conn)
    return df

def get_production():
    query = "SELECT num_peca, tear, peso, product_supplier, check_production, operator, data FROM production"
    df = pd.read_sql(query, con=conn)
    return df

def save(num_peca, peso, tear, operator, product_supplier, check):
    current_date = datetime.now()
    c.execute(
        "INSERT INTO production (num_peca, peso, tear, operator, product_supplier, check_production, data) VALUES (?, ?, ?, ?, ?, ?, ?)", (num_peca, peso, tear, operator, product_supplier, check, current_date)
    )
    conn.commit()


# Sidebar
st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")


# Body
st.title("Registro")
col1, col2 = st.columns([0.4, 0.6])
col3, col4, col5 = st.columns(3)

num_peca = col1.text_input("Número da peça")
peso = col2.number_input("Peso/KG")

df_tear = get_tear()
tear = col3.selectbox("Tear", df_tear["name"].unique())

df_operator = get_operator()
operator = col4.selectbox("Operador", df_operator["name"].unique())

df_product_supplier = get_products_supplier()
product_supplier = col5.selectbox("Fornecedor/Cliente", df_product_supplier["supplier"].unique())

check = st.radio("Verificado ?", ["Sim", "Não"])

insert = st.button("Registrar")

if insert:
    save(num_peca, peso, tear, operator, product_supplier, check)
    df_production = get_production()
    num_peca = ""
    df_production
