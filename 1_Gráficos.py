import pandas as pd
import streamlit as st
import sqlite3
import plotly.express as px


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
    col1, col2 = st.columns(2)
    col1.markdown(f"### Total registrado: {df_filtered['peso'].sum():.2f} Kg")
    col2.markdown(f"### Média: {df_filtered['peso'].mean():.2f} Kg")

    col3, col4 = st.columns(2)
    df_filtered["data"] = pd.to_datetime(df_filtered["data"])
    df_filtered["mes"]  = df_filtered["data"].apply(lambda x:str(x.month))
    month = st.selectbox("Mês", df_filtered["mes"].unique())
    df_filtered_month = df_filtered[df_filtered["mes"] == month]
    df_filtered_month

    df_filtered_month["dia"]  = df_filtered_month["data"].apply(lambda x:str(x.day))
    day = st.selectbox("Dia", df_filtered_month["dia"].unique())
    df_filtered_month_day = df_filtered_month[df_filtered_month["dia"] == day]
    df_filtered_month_day

    df_filtered["hora"] = df_filtered["data"].apply(lambda x:str(x.hour))
    

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