import pandas as pd
import streamlit as st
import sqlite3
import plotly.express as px
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
    query = "SELECT num_peca, tear, peso, supplier, product, check_production, operator, data FROM production"
    df = pd.read_sql(query, con=conn)
    return df


# Sidebar
type_filter = st.sidebar.selectbox("Filtrar por", ["Teares", "Artigo/Produto"])
st.sidebar.divider()
st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")


# Body
df_production = get_production()
df_production["data"] = pd.to_datetime(df_production["data"])

if type_filter == "Teares":
    df_tear = get_tear()
    tear = st.selectbox("Tear", df_tear["name"].unique())
    df_filtered = df_production[df_production["tear"] == tear]
    col1, col2 = st.columns(2)
    col1.markdown(f"### Total registrado: {df_filtered['peso'].sum():.2f} Kg")
    df_filtered["Total"] = df_filtered['peso'].sum()
    fig_tear_operator = px.pie(df_filtered, values="Total", names="product", title="Artigo")
    col2.plotly_chart(fig_tear_operator, use_container_width=True)

if type_filter == "Artigo/Produto":
    df = get_products_supplier()
    product = st.selectbox("Artigo", df["produto"].unique())
    df_filtered = df_production[df_production["product"] == product]
    st.markdown(f"### Total registrado: {df_filtered['peso'].sum():.2f} Kg")
    df_filtered["mes"] = df_filtered["data"].apply(lambda x: str(x.month))
    month = st.selectbox("Mes", df_filtered["mes"].unique())
    df_filtered_month = df_filtered[df_filtered["mes"] == month]
    st.markdown(f"### Total registrado: {df_filtered_month['peso'].sum():.2f} Kg")
    df_filtered_month["dia"] = df_filtered_month["data"].apply(lambda x:str(x.day))
    st.bar_chart(df_filtered_month, x="dia", y="peso", use_container_width=True)