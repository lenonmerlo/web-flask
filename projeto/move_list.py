import urllib.request
import json

def resultado_filmes(tipo):
    if tipo == 'populares':
        url = 'https://api.themoviedb.org/3/movie/popular?api_key=82fcff1143a079117105ad8f3b7ba686&language=pt-BR&page=1'
    elif tipo == 'drama':
        url = 'https://api.themoviedb.org/3/discover/movie?api_key=82fcff1143a079117105ad8f3b7ba686&language=pt-BR&sort_by=popularity.desc&with_genres=18&page=1'

    elif tipo == '2010':
        url = 'https://api.themoviedb.org/3/discover/movie?api_key=82fcff1143a079117105ad8f3b7ba686&language=pt-BR&sort_by=popularity.desc&primary_release_year=2010&page=1'
    else:
        raise ValueError("Tipo inválido. Use 'populares', 'drama' ou '2010'.")

    res = urllib.request.urlopen(url)
    dados = res.read()
    dados_json = json.loads(dados)
    return dados_json['results']
