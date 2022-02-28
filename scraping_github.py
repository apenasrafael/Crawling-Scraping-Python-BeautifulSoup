from bs4 import BeautifulSoup
from crawling import crawl_site
from auxiliar import gerar_csv_github, gerar_json_github


URL = 'https://github.com/trending'
conteudo = crawl_site(URL)
pagina = BeautifulSoup(conteudo, 'html.parser')
limite_de_itens = 10

project_names = pagina.find_all('h1', {'class': 'h3 lh-condensed'}, limit=limite_de_itens)
project_info = pagina.find_all('div', {'class': 'f6 color-fg-muted mt-2'}, limit=limite_de_itens)
projetos = [project_names, project_info]

mensagem = gerar_csv_github(projetos)
print(mensagem)
mensagem = gerar_json_github(projetos)
print(mensagem)
