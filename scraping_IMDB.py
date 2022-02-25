from bs4 import BeautifulSoup
from crawling import crawl_site
from auxiliar import gera_csv_imdb, gera_json_imdb


URL = 'https://www.imdb.com/chart/top/'
conteudo = crawl_site(URL)
pagina = BeautifulSoup(conteudo, 'html.parser')
limite_de_itens = 10

filmes_td_titleColumn = pagina.find_all('td', {'class': 'titleColumn'}, limit=limite_de_itens)
filmes_td_ratingColumn_imdbRating = pagina.find_all('td', {'class': 'ratingColumn imdbRating'}, limit=limite_de_itens)
info_filmes = [filmes_td_titleColumn, filmes_td_ratingColumn_imdbRating]

mensagem = gera_csv_imdb(info_filmes)
print(mensagem)
mensagem = gera_json_imdb(info_filmes)
print(mensagem)
