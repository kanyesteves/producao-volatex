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
operation = st.sidebar.radio("", ["Cadastrar", "Editar", "Remover"])
st.sidebar.divider()
st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")


##################### BODY #####################
if operation == "Cadastrar":
    st.title("Cadastrar")
    st.subheader("Fornecedor/Artigo")
    col1, col2 = st.columns(2)
    supplier  = col1.text_input("Fornecedor/Cliente")
    product   = col2.text_input("Produto")
    save = st.button("Salvar fornecedor")
    if save:
        db.save_product_supplier(supplier, product, False)
        st.toast("Fornecedor/Artigo cadastrado com sucesso!!")

    st.divider()
    st.subheader("Tear")
    col1, col2 = st.columns(2)
    name_tear  = col1.text_input("Nome")
    model_tear = col2.text_input("Modelo")
    save = st.button("Salvar tear")
    if save:
        db.save_tear(name_tear, model_tear, False)
        st.toast("Tear cadastrado com sucesso!!")

    st.divider()
    st.subheader("Operador")
    col1, col2 = st.columns(2)
    name_operator  = col1.text_input("Nome ")
    office_operator = col2.text_input("Cargo")
    save = st.button("Salvar operador")
    if save:
        db.save_operator(name_operator, office_operator, False)
        st.toast("Operador cadastrado com sucesso!!")

else:
    if operation == "Editar":
        st.title("Editar")
    elif operation == "Remover":
        st.title("Remover")


    st.subheader("Produção")
    df_production = db.get_production()
    df = db.get_products_supplier()
    col1, col2 = st.columns(2)
    supplier = col1.selectbox("Fornecedor", df["fornecedor"].unique())
    df_filtered_supplier = df[df["fornecedor"] == supplier]
    product = col2.selectbox("Artigo", df_filtered_supplier["produto"].unique())
    df_filtered = df_production[(df_production["produto"] == product) & (df_production["fornecedor"] == supplier)]
    df_production_not_removed = df_filtered.drop(df_filtered[df_filtered["remove"] == True].index)
    df_production_not_removed = df_production_not_removed.drop("remove", axis=1).copy()
    st.table(df_production_not_removed)

    if operation == "Editar":
        col1, col2, col3 = st.columns([0.5, 1, 2])
        col4, col5, col6, col7 = st.columns([0.5, 1, 1, 2])
        num_peca      = col1.text_input("Numero peça - produção")
        supplier      = col2.text_input("Fornecedor - produção")
        product       = col3.text_input("Produto - produção")
        peso          = col4.number_input("Peso - produção")
        operator      = col5.text_input("Operador - produção")
        tear          = col6.text_input("Tear - produção")
        check         = col7.text_input("Revisão - produção")

        update = st.button("Atualizar registro")
        if update:
            result = db.save_production(num_peca, peso, tear, operator, supplier, product, check, False)
            st.toast("Registro atualizado com sucesso!!")

    elif operation == "Remover":
        col1, col2, col3 = st.columns([0.5, 1, 2])
        col4, col5, col6, col7 = st.columns([0.5, 1, 1, 2])
        num_peca      = col1.text_input("Numero peça - produção")
        supplier      = col2.text_input("Fornecedor - produção")
        product       = col3.text_input("Produto - produção")
        peso          = col4.number_input("Peso - produção")
        operator      = col5.text_input("Operador - produção")
        tear          = col6.text_input("Tear - produção")
        check         = col7.text_input("Revisão - produção")
        delete = st.button("Remover registro")
        if delete:
            result = db.save_production(num_peca, peso, tear, operator, supplier, product, check, True)
            st.toast("Registro removido com sucesso!!")


    st.divider()
    st.subheader("Fornecedor")
    df_products_supplier = db.get_products_supplier()
    df_products_supplier_not_removed = df_products_supplier.drop(df_products_supplier[df_products_supplier["remove"] == True].index)
    df_products_supplier_not_removed = df_products_supplier_not_removed.drop("remove", axis=1).copy()
    st.table(df_products_supplier_not_removed)

    if operation == "Editar":
        col1, col2 = st.columns([2, 2])
        name_supplier  = col1.text_input("Nome - fornecedor")
        name_product   = col2.text_input("Nome - produto")
        update = st.button("Atualizar fornecedor")
        if update:
            db.save_product_supplier(name_supplier, name_product, False)
            st.toast("Fornecedor atualizado name_productm sucesso!!")

    elif operation == "Remover":
        col1, col2 = st.columns([2, 2])
        name_supplier  = col1.text_input("Nome - fornecedor")
        name_product   = col2.text_input("Nome - produto")
        delete = st.button("Remover fornecedor")
        if delete:
            db.save_product_supplier(name_supplier, name_product, True)
            st.toast("Fornecedor removido com sucesso!!")


    st.divider()
    st.subheader("Tear")
    df_tear = db.get_tear()
    df_tear_not_removed = df_tear.drop(df_tear[df_tear["remove"] == True].index)
    df_tear_not_removed = df_tear_not_removed.drop("remove", axis=1).copy()
    st.table(df_tear_not_removed)

    if operation == "Editar":
        col1, col2 = st.columns([2, 2])
        name_tear      = col1.text_input("Nome - tear")
        model          = col2.text_input("Modelo - tear")
        update = st.button("Atualizar tear")
        if update:
            db.save_tear(name_tear, model, False)
            st.toast("Tear atualizado com sucesso!!")

    elif operation == "Remover":
        col1, col2 = st.columns([2, 2])
        name_tear   = col1.text_input("Nome - tear")
        model       = col2.text_input("Modelo - tear")
        delete = st.button("Remover tear")
        if delete:
            db.save_tear(name_tear, model, True)
            st.toast("Tear removido com sucesso!!")


    st.divider()
    st.subheader("Operador")
    df_operator = db.get_operator()
    df_operator_not_removed = df_operator.drop(df_operator[df_operator["remove"] == True].index)
    df_operator_not_removed = df_operator_not_removed.drop("remove", axis=1).copy()
    st.table(df_operator_not_removed)

    if operation == "Editar":
        col1, col2 = st.columns([2, 2])
        name_operator  = col1.text_input("Nome - operador")
        role           = col2.text_input("Cargo - operador")
        update = st.button("Atualizar operador")
        if update:
            db.save_operator(name_operator, role, False)
            st.toast("Operador atualizado com sucesso!!")

    elif operation == "Remover":
        col1, col2 = st.columns([2, 2])
        name_operator  = col1.text_input("Nome - operador")
        role           = col2.text_input("Cargo - operador")
        delete = st.button("Remover operador")
        if delete:
            db.save_operator(name_operator, role, True)
            st.toast("Operador removido com sucesso!!")