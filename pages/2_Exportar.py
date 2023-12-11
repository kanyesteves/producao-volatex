import streamlit as st
import sqlite3
import pandas as pd
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

def df_to_dataset(file_format, df):
    if (file_format == ".csv"):
        return df.to_csv()


#Sidebar
type_filter = st.sidebar.selectbox("Filtrar por", ["Artigo/Produto"])
st.sidebar.divider()
st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")


# Body
st.header("Exportar tabela")

df_production = get_production()
file_export = ""
if type_filter == "Artigo/Produto":
    df = get_products_supplier()

    col1, col2 = st.columns(2)
    supplier = col1.selectbox("Fornecedor", df["supplier"].unique())
    df_filtered_supplier = df[df["supplier"] == supplier]
    product = col2.selectbox("Artigo", df_filtered_supplier["produto"].unique())

    df_filtered = df_production[df_production["product"] == product]
    columns_translated = "Numero-peça Tear Peso Fornecedor Artigo Revisão Operador Data".split()
    df_filtered.columns = columns_translated
    df_filtered

    format_file = st.radio("Formato para exportação:", [".csv"])

    if format_file == ".csv":
        file_export = df_to_dataset(format_file, df_filtered)
    
    
date_now = str(datetime.now())
st.download_button(label="Exportar", 
                    data=file_export, 
                    file_name=f"{supplier}-{product}-{date_now}{format_file}", 
                    mime=f"text/{format_file}")
    