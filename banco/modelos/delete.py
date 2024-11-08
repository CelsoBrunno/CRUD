import streamlit as st

def Delete(cursor, conexao):
    ver_lista = st.radio('Você deseja ver a lista de produtos antes de apagar?', ('Sim', 'Não'))

    if ver_lista == 'Sim':
        comando = 'SELECT * FROM produto'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        
        if resultado:
            st.write("Lista de Produtos:")
            st.table(resultado)
        else:
            st.write("Nenhum produto encontrado.")
    
    opcao = st.selectbox("Escolha um critério para exclusão:", ["Selecione", "ID", "Nome"])
    
    if opcao == "ID":
        id_produto = st.text_input('Informe o ID que deseja apagar:')
        if st.button('Deletar por ID'):
            if id_produto:
                comando = 'DELETE FROM produto WHERE id = %s;'
                cursor.execute(comando, (id_produto,))
                conexao.commit()
                st.success('Produto com ID deletado com sucesso.')
            else:
                st.error('Por favor, insira um ID válido.')
    
    elif opcao == "Nome":
        nome_produto = st.text_input('Informe o nome que deseja apagar:')
        if st.button('Deletar por Nome'):
            if nome_produto:
                comando = 'DELETE %s;'
                cursor.execute(comando, (nome_produto,))
                conexao.commit()
                st.success('Produto com nome deletado com sucesso.')
            else:
                st.error('Por favor, insira um nome válido.')
    else:
        st.warning('Por favor, selecione uma opção válida para exclusão.')
