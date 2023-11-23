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


# Sidebar
register = st.sidebar.selectbox("Cadastrar", ["Tear", "Operador", "Fornecedor/Produto"])
st.sidebar.divider()
st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")


# Funções
def save_tear(name_tear, model_tear):
    current_date = datetime.now()
    c.execute(
        "INSERT INTO teares (name, model, created_at) VALUES (?, ?, ?)", (name_tear,  model_tear, current_date)
    )
    conn.commit()
    name_tear = ""
    model_tear = ""

def save_operator(name_operator, office_operator):
    current_date = datetime.now()
    c.execute(
        "INSERT INTO operators (name, office, created_at) VALUES (?, ?, ?)", (name_operator,  office_operator, current_date)
    )
    conn.commit()
    name_operator = ""
    office_operator = ""

def save_product_supplier(supplier, product):
    current_date = datetime.now()
    c.execute(
        "INSERT INTO products_suppliers (supplier, produto, created_at) VALUES (?, ?, ?)", (supplier,  product, current_date)
    )
    conn.commit()
    supplier = ""
    product = ""


# Body
if register == "Tear":
    st.title("Cadastrar Tear :toolbox:")
    col1, col2 = st.columns(2)
    name_tear  = col1.text_input("Nome")
    model_tear = col2.text_input("Modelo")
    save = st.button("Salvar")
    if save:
        save_tear(name_tear, model_tear)

if register == "Operador":
    st.title("Cadastrar Operador :male-factory-worker:")
    col1, col2 = st.columns(2)
    name_operator  = col1.text_input("Nome")
    office_operator = col2.text_input("Cargo")
    save = st.button("Salvar")
    if save:
        save_operator(name_operator, office_operator)

if register == "Fornecedor/Produto":
    st.title("Cadastrar Fornecedor/Cliente :factory:")
    col1, col2 = st.columns(2)
    supplier  = col1.text_input("Fornecedor/Cliente")
    product = col2.text_input("Produto")
    save = st.button("Salvar")
    if save:
        save_product_supplier(supplier, product)