import pandas as pd
import streamlit as st
from services import Services

st.set_page_config(
    layout="wide",
    page_title="Produção-Volatex"
)

# Variáveis Globais
db = Services()

##################### Sidebar #####################
st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")


##################### BODY #####################
st.title("Registro")
df_tear = db.get_tear()
tear = st.selectbox("Tear", df_tear["nome"].unique())
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

df_product_supplier = db.get_products_supplier()
supplier    = col1.selectbox("Fornecedor", df_product_supplier["fornecedor"].unique())
supplier_filtered = df_product_supplier[df_product_supplier["fornecedor"] == supplier]
product     = col2.selectbox("Artigo", supplier_filtered["produto"].unique())
num_peca    = col3.text_input("Número da peça")
peso        = col4.number_input("Peso/KG")
df_operator = db.get_operator()
operator    = col5.selectbox("Operador", df_operator["nome"].unique())
check       = st.text_input("Revisão")
insert      = st.button("Registrar")
if insert:
    result = db.save_production(num_peca, peso, tear, operator, supplier, product, check, False)
    st.toast("Resgistrado com sucesso !!")


df_production          = db.get_production()
df_production_tear     = df_production[df_production["tear"] == tear]
df_production_supplier = df_production_tear[df_production_tear["fornecedor"] == supplier]
df_production_filtered = df_production_supplier[df_production_supplier["produto"] == product]
df_production_not_removed = df_production_filtered.drop(df_production_filtered[df_production_filtered["remove"] == True].index)
df_production_not_removed = df_production_not_removed.drop("remove", axis=1).copy()

try:
    st.markdown("## Último registro")
    col1, col2 = st.columns(2)
    col1.markdown(f"**Número da peça**: {df_production_not_removed.iloc[-1]['num_peça']}")
    col1.markdown(f"**Tear**:           {df_production_not_removed.iloc[-1]['tear']}")
    col1.markdown(f"**Fornecedor**:     {df_production_not_removed.iloc[-1]['fornecedor']}")
    col1.markdown(f"**Artigo**:         {df_production_not_removed.iloc[-1]['produto']}")
    col2.markdown(f"**Peso**:           {df_production_not_removed.iloc[-1]['peso']}")
    col2.markdown(f"**Operador**:       {df_production_not_removed.iloc[-1]['operador']}")
    col2.markdown(f"**Revisão**:        {df_production_not_removed.iloc[-1]['revisao']}")

except Exception as er:
    st.warning("Nenhum registro cadastrado nesse artigo !!")
