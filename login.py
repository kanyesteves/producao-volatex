import streamlit as st
import sqlite3

st.set_page_config(
    layout="wide",
    page_title="Produção-Volatex"
)


# Variáveis Globais
conn = sqlite3.connect("db/db_producao.db")
c = conn.cursor()


# Funções
def verificar_login(username, password):
    query = "SELECT user_type FROM users WHERE username = ? AND password = ?"
    result = c.execute(query, (username, password)).fetchone()
    return result[0] if result else None


# Body
st.header("Volatex - Produção")
st.subheader("Sistema de controle para produção")
username_input = st.text_input("Usuário")
password_input = st.text_input("Senha", type="password")
login_button = st.button("Login")

if login_button:
    tipo_usuario = verificar_login(username_input, password_input)
    if tipo_usuario:
        st.session_state.tipo_usuario = tipo_usuario
        st.success(f"Login bem-sucedido!!")
    else:
        st.error("Usuário ou senha incorretos.")
