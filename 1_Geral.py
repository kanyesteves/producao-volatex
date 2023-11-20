import pandas as pd
import streamlit as st
import sqlite3
import numpy as np

conn = sqlite3.connect("db/db_producao.db")

st.set_page_config(
    layout="wide",
    page_title="Produção-Volatex"
)

# Variaveis
tear_list = ["Todos", "Tear 1", "Tear 2", "Tear 3"]
mes_list = np.arange(13)
dia_list = np.arange(32)
product_list = ["Elian", "RVB", "Angero"]

# Sidebar
tear = st.sidebar.selectbox("Tear", tear_list)
st.sidebar.divider()
st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")

# Body
col1, col2 = st.columns(2)
if tear != "Todos":
    st.selectbox("Cliente/Produto", product_list)
    col1.selectbox("Mês", mes_list)
    col2.selectbox("Dia", dia_list)