import streamlit as st
import pandas as pd
from datetime import datetime
from services import Services


st.set_page_config(
    layout="wide",
    page_title="Produção-Volatex"
)

# Variáveis Globais
db = Services()


##################### Sidebar #####################
type_filter = st.sidebar.selectbox("Filtrar por", ["Artigo/Produto"])
st.sidebar.divider()

if st.sidebar.button("Logout"):
    st.session_state.login = False
    st.switch_page("login.py")

st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")


##################### Funções #####################
def df_to_dataset(file_format, df):
    if (file_format == ".csv"):
        return df.to_csv()


##################### BODY #####################
def main():
    st.title("Exportar tabela")
    df_production = db.get_production()
    file_export = ""
    if type_filter == "Artigo/Produto":
        df = db.get_products_supplier()


        col1, col2 = st.columns(2)
        df_production_not_removed = df.drop(df[df["remove"] == True].index)
        df_production_not_removed = df_production_not_removed.drop("remove", axis=1).copy()
        supplier = col1.selectbox("Fornecedor", df_production_not_removed["fornecedor"].unique())
        df_filtered_supplier = df_production_not_removed[df["fornecedor"] == supplier]
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



# Verifica permissão
if not st.session_state.get("login"):
    st.error("Sessão expirada, faça o login novamente.")
    if st.button("Ir para tela de login"):
        st.switch_page("login.py")
else:
    main()
    