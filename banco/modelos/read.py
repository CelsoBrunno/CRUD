import streamlit as st

def Read(cursor, conexao):
    st.write("Listando todos os produtos:")
    comando = f'SELECT * FROM alunos'
    cursor.execute(comando)
    resultado = cursor.fetchall() # ler o banco de dados
    st.write(resultado)

