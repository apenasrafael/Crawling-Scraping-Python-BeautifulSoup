# Crawling-e-Scraping-com-Python
Olá!

Esse é um projeto de estudo de Crawling e Scraping com Python utilizando as bibliotecas **BeautifulSoup**, **requests** e **json**

**crawling.py** faz a requisição ao site e devolve o conteúdo (HTML) da página. 

**scraping_IMDB.py** solicita a leitura do site com os [TOP 250](https://www.imdb.com/chart/top/) filmes do IMDB, ordenados pela nota. Para simplificar o processamento, foi determinado que somente os 10 primeiros filmes sejam buscados. Esse valor pode ser alterado na variável **limite_de_itens**  

**scraping_github.py** solicita a leitura do [Trending](https://github.com/trending) do GitHub. Nesse caso, também foi limitado para os 10 primeiros, sendo possível alterar na variável **limite_de_itens**  

**auxiliar.py** possui funções para gerar **JSON** ou **CSV**, tanto para o IMDB quanto para o GitHub

**requirements.txt** lista as bibliotecas instaladas (e suas respectivas dependências).
