import pandas as pd
import streamlit as st
import sqlite3


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


# Sidebar
type_filter = st.sidebar.selectbox("Filtrar por", ["Teares", "Operadores", "Fornecedor/Produto"])
st.sidebar.divider()
st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")


# Body
df_production = get_production()

if type_filter == "Teares":
    df_tear = get_tear()
    tear = st.selectbox("Tear", df_tear["name"].unique())
    df_filtered = df_production[df_production["tear"] == tear]
    st.markdown(f"## Total registrado: {df_filtered['peso'].sum():.2f} Kg")
    st.markdown(f"## Média: {df_filtered['peso'].mean():.2f} Kg")
    

if type_filter == "Operadores":
    df = get_operator()
    operator = st.selectbox("Operador", df["name"].unique())
    df_filtered = df_production[df_production["operator"] == operator]
    df_filtered

if type_filter == "Fornecedor/Produto":
    df = get_products_supplier()
    products_supplier = st.selectbox("Fornecedor/Cliente", df["supplier"].unique())
    df_filtered = df_production[df_production["product_supplier"] == products_supplier]
    df_filtered