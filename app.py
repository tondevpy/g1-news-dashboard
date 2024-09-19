import requests
from bs4 import BeautifulSoup
import streamlit as st

# Função para obter as notícias
def get_news(termo):
    url = 'https://www.globo.com/'

    # Realizar a requisição
    page = requests.get(url)

    # Usando o BeautifulSoup para organizar o retorno HTML
    soup = BeautifulSoup(page.text, 'html.parser')

    # Encontrar todas as tags <a> que possam conter títulos
    noticias = soup.find_all('a')

    results = []
    for noticia in noticias:
        titulo = noticia.find('h2')  # Verificar se existe uma tag <h2>
        if titulo:
            link = noticia['href']  # Extrair o link diretamente da tag <a>
            if termo.lower() in titulo.text.lower():  # Busca case-insensitive
                results.append((titulo.text, link))
    return results

# Título do site
st.title("Globo News - TonDevPy")

# Cabeçalho
st.header("Seja bem vindo, faça sua pesquisa...")

# Seção de busca de notícias
st.header("Busca de Notícias na Globo.com")

# Input para o termo de pesquisa
termo = st.text_input("Digite um termo para buscar notícias na Globo.com:")

# Botão de busca
if st.button("Buscar Notícias"):
    if termo:
        # Exibir um indicador de carregamento
        with st.spinner('Buscando notícias...'):
            noticias = get_news(termo)

        if noticias:
            st.success(f"Encontramos {len(noticias)} notícia(s)!")
            for titulo, link in noticias:
                st.write(f"**{titulo}**")
                st.write(f"[Clique aqui para ler a notícia]({link})")
        else:
            st.error("Nenhuma notícia encontrada com o termo fornecido.")
    else:
        st.error("Por favor, insira um termo de pesquisa.")
