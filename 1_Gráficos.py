import pandas as pd
import streamlit as st
import sqlite3
import numpy as np

st.set_page_config(
    layout="wide",
    page_title="SysProduct-Volatex"
)

# Variáveis Globais
conn = sqlite3.connect("db/db_producao.db")
c = conn.cursor()

# Variaveis

# Sidebar
type_filter = st.sidebar.selectbox("Filtrar por", ["Teares", "Operadores", "Fornecedor/Produto"])
st.sidebar.divider()
st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")

# Body
col1, col2 = st.columns(2)
if type_filter == "Teares":
    st.title(":male-factory-worker: Em Desenvolvimento... ")


if type_filter == "Operadores":
    st.title(":male-office-worker: Em Desenvolvimento... ")


if type_filter == "Fornecedor/Produto":
    st.title(":male-construction-worker: Em Desenvolvimento... ")