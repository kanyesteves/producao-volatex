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
type_filter = st.sidebar.selectbox("Filtrar por", ["Teares", "Artigo/Produto"])
st.sidebar.divider()

if st.sidebar.button("Logout"):
    st.session_state.login = False
    st.switch_page("login.py")

st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")

##################### BODY #####################
def main():
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
        try:
            st.bar_chart(df_filtered_month, x="dia", y="peso", color="produto", use_container_width=True)
        except Exception as er:
            st.warning(f"Nenhum dado registrado no {tear}")


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
        try:
            st.bar_chart(df_filtered_month, x="dia", y="peso", use_container_width=True)
        except Exception as er:
            st.warning(f"Erro ao criar gráfico")



# Verifica permissão
if not st.session_state.get("login"):
    st.error("Sessão expirada, faça o login novamente.")
    if st.button("Ir para tela de login"):
        st.switch_page("login.py")
else:
    main()