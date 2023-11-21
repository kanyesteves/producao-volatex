import pandas as pd
import streamlit as st
import sqlite3
import numpy as np

conn = sqlite3.connect("db/db_producao.db")

st.set_page_config(
    layout="wide",
    page_title="SysProduct-Volatex"
)

# Variaveis

# Sidebar
st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")

# Body
col1, col2 = st.columns(2)
