import pandas as pd
import streamlit as st
import sqlite3

conn = sqlite3.connect("db/db_producao.db")

st.set_page_config(
    layout="wide",
    page_title="SysProduct-Volatex"
)

# Sidebar
st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")

# Body