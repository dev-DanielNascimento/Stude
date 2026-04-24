import psycopg2

@st.cache_resource #mantém o cache de conexão do streamlit
def inicia_conexao():
    psycopg2.connect(
        host=;
        port=;
        database=;
        user=;
        password=;
    )