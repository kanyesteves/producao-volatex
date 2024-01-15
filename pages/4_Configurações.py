import pandas as pd
import streamlit as st
import sqlite3
from datetime import datetime
from lib import Functions


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
db = Functions(conn)


##################### Sidebar #####################
operation = st.sidebar.radio("", ["Cadastrar", "Editar"])
st.sidebar.divider()
st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")


##################### Funções #####################
def save_tear(name_tear, model_tear):
    current_date = datetime.now()
    c.execute(
        "INSERT INTO teares (name, model, created_at) VALUES (?, ?, ?)", (name_tear,  model_tear, current_date)
    )
    conn.commit()

def save_operator(name_operator, office_operator):
    current_date = datetime.now()
    c.execute(
        "INSERT INTO operators (name, office, created_at) VALUES (?, ?, ?)", (name_operator,  office_operator, current_date)
    )
    conn.commit()

def save_product_supplier(supplier, product):
    current_date = datetime.now()
    c.execute(
        "INSERT INTO products_suppliers (supplier, produto, created_at) VALUES (?, ?, ?)", (supplier,  product, current_date)
    )
    conn.commit()

def update_production(id_peca, column_table, value):
    query = f"UPDATE production SET {column_table} = ? WHERE id = ?"
    c.execute(
        query, (value, id_peca)
    )
    conn.commit()

def update_products_supplier(id_supplier, column_table, value):
    query = f"UPDATE products_suppliers SET {column_table} = ? WHERE id = ?"
    c.execute(
        query, (value, id_supplier)
    )
    conn.commit()

def update_tear(id_tear, column_table, value):
    query = f"UPDATE teares SET {column_table} = ? WHERE id = ?"
    c.execute(
        query, (value, id_tear)
    )
    conn.commit()

def update_operator(id_operator, column_table, value):
    query = f"UPDATE operators SET {column_table} = ? WHERE id = ?"
    c.execute(
        query, (value, id_operator)
    )
    conn.commit()


##################### BODY #####################
if operation == "Cadastrar":
    st.title("Cadastrar")
    st.subheader("Fornecedor/Artigo")
    col1, col2 = st.columns(2)
    supplier  = col1.text_input("Fornecedor/Cliente")
    product = col2.text_input("Produto")
    save = st.button("Salvar fornecedor")
    if save:
        save_product_supplier(supplier, product)
        st.success("Fornecedor/Artigo cadastrado com sucesso!!")

    st.divider()
    st.subheader("Tear")
    col1, col2 = st.columns(2)
    name_tear  = col1.text_input("Nome")
    model_tear = col2.text_input("Modelo")
    save = st.button("Salvar tear")
    if save:
        save_tear(name_tear, model_tear)
        st.success("Tear cadastrado com sucesso!!")

    st.divider()
    st.subheader("Operador")
    col1, col2 = st.columns(2)
    name_operator  = col1.text_input("Nome ")
    office_operator = col2.text_input("Cargo")
    save = st.button("Salvar operador")
    if save:
        save_operator(name_operator, office_operator)
        st.success("Operador cadastrado com sucesso!!")

if operation == "Editar":
    st.title("Editar")

    st.subheader("Produção")
    df_production = db.get_production()
    df = db.get_products_supplier()
    col1, col2 = st.columns(2)
    supplier = col1.selectbox("Fornecedor", df["supplier"].unique())
    df_filtered_supplier = df[df["supplier"] == supplier]
    product = col2.selectbox("Artigo", df_filtered_supplier["produto"].unique())
    df_filtered = df_production[(df_production["product"] == product) & (df_production["supplier"] == supplier)]
    df_filtered = df_filtered.set_index("id")
    st.table(df_filtered)
    col3, col4, col5 = st.columns([1, 2, 3])
    id_peca      = col3.text_input("ID - produção")
    column_table = col4.selectbox("Coluna - produção", ["num_peca", "peso", "supplier", "product", "check_production", "operator"])
    if column_table == "peso":
        value = col5.number_input("Valor - produção")
    else:
        value = col5.text_input("Valor - produção")

    update = st.button("Atualizar registro")
    if update:
        update_production(id_peca, column_table, value)
        st.success("Registro atualizado com sucesso!!")
        

    st.divider()
    st.subheader("Fornecedor")
    df_products_supplier = db.get_products_supplier()
    df = df_products_supplier.set_index("id")
    st.table(df)
    col6, col7, col8 = st.columns([1, 2, 3])
    id_supplier  = col6.text_input("ID - fornecedor")
    column_table = col7.selectbox("Coluna - fornecedor", ["supplier", "produto"])
    value        = col8.text_input("Valor - fornecedor")
    update = st.button("Atualizar fornecedor")
    if update:
        update_products_supplier(id_supplier, column_table, value)
        st.success("Fornecedor atualizado com sucesso!!")


    st.divider()
    st.subheader("Tear")
    df_tear = db.get_tear()
    df = df_tear.set_index("id")
    st.table(df)
    col9, col10, col11 = st.columns([1, 2, 3])
    id_tear      = col9.text_input("ID - tear")
    column_table = col10.selectbox("Coluna - tear", ["name", "model"])
    value        = col11.text_input("Valor - tear")
    update = st.button("Atualizar tear")
    if update:
        update_tear(id_tear, column_table, value)
        st.success("Tear atualizado com sucesso!!")


    st.divider()
    st.subheader("Operador")
    df_operator = db.get_operator()
    df = df_operator.set_index("id")
    st.table(df)
    col12, col13, col14 = st.columns([1, 2, 3])
    id_operator  = col12.text_input("ID - operador")
    column_table = col13.selectbox("Coluna - operador", ["name", "office"])
    value        = col14.text_input("Valor - operador")
    update = st.button("Atualizar operador")
    if update:
        update_operator(id_operator, column_table, value)
        st.success("Operador atualizado com sucesso!!")