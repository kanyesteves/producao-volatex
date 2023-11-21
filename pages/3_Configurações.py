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


def get_tear():
    c.execute(
        "SELECT name, model, created_at FROM teares"
    )


# Body
col1, col2 = st.columns(2)
if register == "Tear":
    name_tear  = col1.text_input("Nome")
    model_tear = col2.text_input("Modelo")
    save = st.button("Salvar")
    if save:
        save_tear(name_tear, model_tear)
        get_tear()


if register == "Operador":
    name_operator  = col1.text_input("Nome")
    office_operator = col2.text_input("Cargo")
    save = st.button("Salvar")


if register == "Fornecedor/Produto":
    name_product_supplier  = col1.text_input("Nome")
    office_product_supplier = col2.text_input("Produto")
    save = st.button("Salvar")