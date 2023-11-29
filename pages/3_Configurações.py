import pandas as pd
import streamlit as st
import sqlite3
from datetime import datetime


st.set_page_config(
    layout="wide",
    page_title="Produção-Volatex"
)


# Verifica permissão
if st.session_state.get("tipo_usuario") != "admin":
    st.error("Você não tem permissão para acessar esta página.")
    st.stop()


# Variáveis Globais
conn = sqlite3.connect("db/db_producao.db")
c = conn.cursor()


# Sidebar
register = st.sidebar.selectbox("Cadastrar", ["Tear", "Operador", "Fornecedor/Artigo"])
st.sidebar.divider()
st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")


# Funções
def save_tear(name_tear, model_tear):
    current_date = datetime.now()
    c.execute(
        "INSERT INTO teares (name, model, created_at) VALUES (?, ?, ?)", (name_tear,  model_tear, current_date)
    )
    conn.commit()

def save_operator(name_operator, office_operator):
    current_date = datetime.now()
    c.execute(
        "INSERT INTO operators (name, office, created_at) VALUES (?, ?, ?)", (name_operator,  office_operator, current_date)
    )
    conn.commit()

def save_product_supplier(supplier, product):
    current_date = datetime.now()
    c.execute(
        "INSERT INTO products_suppliers (supplier, produto, created_at) VALUES (?, ?, ?)", (supplier,  product, current_date)
    )
    conn.commit()


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

if register == "Fornecedor/Artigo":
    st.title("Cadastrar Fornecedor/Artigo :factory:")
    col1, col2 = st.columns(2)
    supplier  = col1.text_input("Fornecedor/Cliente")
    product = col2.text_input("Produto")
    save = st.button("Salvar")
    if save:
        save_product_supplier(supplier, product)