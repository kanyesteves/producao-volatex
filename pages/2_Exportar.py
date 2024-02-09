import streamlit as st
import pandas as pd
from datetime import datetime
from services import Services


st.set_page_config(
    layout="wide",
    page_title="Produção-Volatex"
)

# Verifica permissão
if st.session_state.get("tipo_usuario") != "admin":
    st.error("Você não tem permissão para acessar esta página.")
    st.stop()


# Variáveis Globais
db = Services()


##################### Sidebar #####################
type_filter = st.sidebar.selectbox("Filtrar por", ["Artigo/Produto"])
st.sidebar.divider()
st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")


##################### Funções #####################
def df_to_dataset(file_format, df):
    if (file_format == ".csv"):
        return df.to_csv()


##################### BODY #####################
st.title("Exportar tabela")
df_production = db.get_production()
file_export = ""
if type_filter == "Artigo/Produto":
    df = db.get_products_supplier()


    col1, col2 = st.columns(2)
    supplier = col1.selectbox("Fornecedor", df["fornecedor"].unique())
    df_filtered_supplier = df[df["fornecedor"] == supplier]
    product = col2.selectbox("Artigo", df_filtered_supplier["produto"].unique())

    df_filtered = df_production[(df_production["produto"] == product) & (df_production["fornecedor"] == supplier)]
    df_production_not_removed = df_filtered.drop(df_filtered[df_filtered["remove"] == True].index)
    df_production_not_removed = df_production_not_removed.drop("remove", axis=1).copy()
    st.table(df_production_not_removed)

    format_file = ".csv"
    file_export = df_to_dataset(format_file, df_filtered)
    
date = datetime.now()
date_now = date.strftime("%Y-%m-%d")
st.download_button(label="Exportar", data=file_export, 
                    file_name=f"{supplier}-{product}-{date_now}{format_file}", 
                    mime=f"text/{format_file}")
    