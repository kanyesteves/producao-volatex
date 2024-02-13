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

    df_production_not_removed = df_tear.drop(df_tear[df_tear["remove"] == True].index)
    df_production_not_removed = df_production_not_removed.drop("remove", axis=1).copy()
    tear = st.selectbox("Tear", df_production_not_removed["nome"].unique())
    df_filtered = df_production[df_production["tear"] == tear]

    st.markdown(f"### Total registrado: {df_filtered['peso'].sum():.2f} Kg")

    df_filtered["mes"] = df_filtered["data"].apply(lambda x: str(x.month))
    month = st.selectbox("Mes", df_filtered["mes"].unique())
    df_filtered_month = df_filtered[df_filtered["mes"] == month]

    st.markdown(f"### Total do mês registrado: {df_filtered_month['peso'].sum():.2f} Kg")
    df_filtered_month["dia"] = df_filtered_month["data"].apply(lambda x:str(x.day))
    st.bar_chart(df_filtered_month, x="dia", y="peso", color="produto", use_container_width=True)



if type_filter == "Artigo/Produto":
    df = db.get_products_supplier()

    col1, col2 = st.columns(2)
    df_production_not_removed = df.drop(df[df["remove"] == True].index)
    df_production_not_removed = df_production_not_removed.drop("remove", axis=1).copy()
    supplier = col1.selectbox("Fornecedor", df_production_not_removed["fornecedor"].unique())
    df_filtered_supplier = df_production_not_removed[df_production_not_removed["fornecedor"] == supplier]
    product = col2.selectbox("Artigo", df_filtered_supplier["produto"].unique())
    df_filtered = df_production[(df_production["produto"] == product) & (df_production["fornecedor"] == supplier)]

    st.markdown(f"### Total registrado: {df_filtered['peso'].sum():.2f} Kg")

    df_filtered["mes"] = df_filtered["data"].apply(lambda x: str(x.month))
    month = st.selectbox("Mes", df_filtered["mes"].unique())
    df_filtered_month = df_filtered[df_filtered["mes"] == month]

    st.markdown(f"### Total do mês registrado: {df_filtered_month['peso'].sum():.2f} Kg")
    df_filtered_month["dia"] = df_filtered_month["data"].apply(lambda x:str(x.day))
    st.bar_chart(df_filtered_month, x="dia", y="peso", use_container_width=True)