import json
from datetime import datetime


def gerar_csv_imdb(info_filmes):
    filmes_td_titleColumn = info_filmes[0]
    filmes_td_ratingColumn_imdbRating = info_filmes[1]
    cabecalho = 'ranking;titulo;ano;nota\n'
    itens = list()

    for i in range(len(filmes_td_titleColumn)):
        filme = filmes_td_titleColumn[i].getText().strip().split()
        nota = filmes_td_ratingColumn_imdbRating[i].getText().strip().split()[0]
        posicao = filme[0].replace('.', '')
        titulo = ' '.join(filme[1:-1])
        ano = filme[-1].replace('(', '').replace(')', '')
        registro = f'{posicao};{titulo};{ano};{nota}'
        itens.append(registro)

    mensagem = gerar_csv('imdb.csv', cabecalho, itens)
    return mensagem


def gerar_json_imdb(info_filmes):
    filmes_td_titleColumn = info_filmes[0]
    filmes_td_ratingColumn_imdbRating = info_filmes[1]
    dicionario = dict()
    for i in range(len(filmes_td_titleColumn)):
        aux = dict()
        filme = filmes_td_titleColumn[i].getText().strip().split()
        nota = filmes_td_ratingColumn_imdbRating[i].getText().strip().split()[0]
        diretor = filmes_td_titleColumn[i].find('a')
        diretor = str(diretor).split(',')[0]
        diretor = diretor[diretor.find('title="') + 7:diretor.find('(') - 1]
        posicao = filme[0].replace('.', '')
        titulo = ' '.join(filme[1:-1])
        ano = filme[-1].replace('(', '').replace(')', '')
        aux['titulo'] = titulo
        aux['nota'] = nota
        aux['diretor'] = diretor
        aux['ano'] = ano
        dicionario[posicao] = aux

    return json.dumps(dicionario, indent=2, ensure_ascii=False)


def gerar_csv_github(projetos):
    project_names = projetos[0]
    project_info = projetos[1]
    cabecalho = 'ranking;project;language;stars;stars_today;forks\n'
    itens = list()

    for i in range(len(project_names)):
        nomes = project_names[i].getText().strip().split()
        info = project_info[i].getText().strip().split()
        if len(info) == 7:
            info.insert(0, '')
        registro = f'{i + 1};{nomes[2]};{info[0]};{info[1]};{info[2]};{info[5]}'
        itens.append(registro)

    mensagem = gerar_csv('github.csv', cabecalho, itens)
    return mensagem


def gerar_json_github(projetos):
    project_names = projetos[0]
    project_info = projetos[1]
    dicionario = dict()
    for i in range(len(project_names)):
        aux = dict()
        nomes = project_names[i].getText().strip().split()
        info = project_info[i].getText().strip().split()
        if len(info) == 7:
            info.insert(0, '')
        aux['project'] = nomes[2]
        aux['language'] = info[0]
        aux['stars'] = info[1]
        aux['stars_today'] = info[2]
        aux['forks'] = info[5]
        dicionario[i+1] = aux
        dicionario['data_de_consulta'] = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

    return json.dumps(dicionario, indent=2, ensure_ascii=False)


def gerar_csv(nome_arquivo, cabecalho, itens):
    with open(file=nome_arquivo, mode='w', encoding='utf8') as arquivo:
        arquivo.write(cabecalho)
        for item in itens:
            arquivo.write(item + '\n')

    return f'Arquivo {nome_arquivo} criado com sucesso!'
