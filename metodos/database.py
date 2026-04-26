import psycopg2
import streamlit as st
import os

@st.cache_resource #mantém o cache de conexão do streamlit
def inicia_conexao():
    psycopg2.connect(
        host=os.getenv("host"),
        user=os.getenv("user"),
        password=os.getenv("password"),
        dbname=os.getenv("dbname")
    )

con = inicia_conexao()

#def criar_tabelas():
#    with con.cursor() as cur:
#        CREATE TABLE IF NOT EXISTS 