import pandas as pd
import streamlit as st
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
type_filter = st.sidebar.selectbox("Filtrar por", ["Teares", "Artigo/Produto"])
st.sidebar.divider()
st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")


##################### BODY #####################
df_production = db.get_production()
df_production["data"] = pd.to_datetime(df_production["data"])

if type_filter == "Teares":
    df_tear = db.get_tear()

    tear = st.selectbox("Tear", df_tear["nome"].unique())
    df_filtered = df_production[df_production["tear"] == tear]
    df_production_not_removed = df_filtered.drop(df_filtered[df_filtered["remove"] == True].index)
    df_production_not_removed = df_production_not_removed.drop("remove", axis=1).copy()

    st.markdown(f"### Total registrado: {df_production_not_removed['peso'].sum():.2f} Kg")

    df_production_not_removed["mes"] = df_production_not_removed["data"].apply(lambda x: str(x.month))
    month = st.selectbox("Mes", df_production_not_removed["mes"].unique())
    df_filtered_month = df_production_not_removed[df_production_not_removed["mes"] == month]

    st.markdown(f"### Total do mês registrado: {df_filtered_month['peso'].sum():.2f} Kg")
    df_filtered_month["dia"] = df_filtered_month["data"].apply(lambda x:str(x.day))
    st.bar_chart(df_filtered_month, x="dia", y="peso", color="produto", use_container_width=True)

if type_filter == "Artigo/Produto":
    df = db.get_products_supplier()

    col1, col2 = st.columns(2)
    supplier = col1.selectbox("Fornecedor", df["fornecedor"].unique())
    df_filtered_supplier = df[df["fornecedor"] == supplier]
    product = col2.selectbox("Artigo", df_filtered_supplier["produto"].unique())
    df_filtered = df_production[(df_production["produto"] == product) & (df_production["fornecedor"] == supplier)]
    df_production_not_removed = df_filtered.drop(df_filtered[df_filtered["remove"] == True].index)
    df_production_not_removed = df_production_not_removed.drop("remove", axis=1).copy()

    st.markdown(f"### Total registrado: {df_production_not_removed['peso'].sum():.2f} Kg")

    df_production_not_removed["mes"] = df_production_not_removed["data"].apply(lambda x: str(x.month))
    month = st.selectbox("Mes", df_production_not_removed["mes"].unique())
    df_filtered_month = df_production_not_removed[df_production_not_removed["mes"] == month]

    st.markdown(f"### Total do mês registrado: {df_filtered_month['peso'].sum():.2f} Kg")
    df_filtered_month["dia"] = df_filtered_month["data"].apply(lambda x:str(x.day))
    st.bar_chart(df_filtered_month, x="dia", y="peso", use_container_width=True)