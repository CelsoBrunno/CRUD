import streamlit as st

def Update(cursor, conexao):
    st.write("Atualizar o preço de um produto:")
    
    produto = st.text_input('Digite o nome do produto:')
    
    valor = st.number_input('Informe o novo valor do produto:', min_value=0, step=1)
    
    if st.button('Atualizar Produto'):
        if produto and valor > 0:
            comando = f'UPDATE produto SET preco = {valor} WHERE nome = "{produto}"'
            cursor.execute(comando)
            conexao.commit()
            st.success(f'O preço do produto {produto} foi atualizado para {valor}.')
        else:
            st.error("Por favor, insira um nome de produto válido e um valor maior que zero.")
