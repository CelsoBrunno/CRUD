import streamlit as st

def Create(cursor, conexao):
    st.write("Cadastro de novo produto")
    
    nome = st.text_input('Informe o nome do produto:')
    
    preco = st.number_input('Informe o valor do produto:', min_value=0.0, step=0.01, format="%.2f")
    
    if st.button('Cadastrar Produto'):
        if nome and preco > 0:
            comando = 'INSERT INTO VALUES (%s, %s)'
            cursor.execute(comando, (nome, preco))
            conexao.commit()
            st.success('Produto cadastrado com sucesso.')
        else:
            st.error("Por favor, insira um nome válido e um preço maior que zero.")
