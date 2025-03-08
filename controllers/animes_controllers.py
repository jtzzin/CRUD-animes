from models.animes_models import Anime
from db import db
import json
from flask import make_response, request


def get_animes():
    animes= Anime.query.all()
    
    if not animes:
        response = make_response(
            json.dumps({
                'mensagem':'nenhum anime encontrado',
                'dados': []
            },ensure_ascii=False,sort_keys=False)
        )
    else:
        response = make_response(
            json.dumps({
                'mensagem':'Lista de animes',
                'dados': [anime.json() for anime in animes]
            },ensure_ascii=False,sort_keys=False)
        )
    response.headers['Content-Type'] = 'application/json'
    return response


def get_anime_by_id(anime_id):
    anime = Anime.query.get(anime_id)
        
    if anime:
        response = make_response(
            json.dumps({
                'mensagem':'anime encontrado',
                'dados': anime.json()
            },ensure_ascii, sort_keys=False)
        )
        response.headers['Content-Type'] ='application/json'
        return response
    else:
        response = make_response(
            json.dumps({
                'mensagem':'anime não encontrado',
                'dados':{}
            },ensure_ascii=False), 
            404 
        )
        response.headers['Content-Type'] ='application/json'
        return response
        
        
def get_anime_by_titulo(titulo_anime):
    anime = Anime.query.filter_by(titulo=titulo_anime).first() # busca o primeiro
   
    if anime:
        response = make_response(
            json.dumps({
                'mensagem':'anime encontrado',
                'dados': anime.json()
            },sort_keys=False)
        )
        response.headers['Content-Type'] ='application/json'
        return response
    else:
        response = make_response(
            json.dumps({
                'mensagem':'anime não encontrado',
                'dados':{}
            },sort_keys=False)
        )
        response.headers['Content-Type'] ='application/json'
        return response, 404
    

def create_anime(anime_data):
    if not all(key in anime_data for key in ['titulo','genero','estudio', 'temporada']):
        response = make_response(
            json.dumps({'mensagem': 'Dados invalidos.Titulo, genero e salário são obrigatórios.'},ensure_ascii=False),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    
    novo_anime = Anime(
        titulo = anime_data['titulo'],    
        genero = anime_data['genero'],
        estudio = anime_data['estudio'],
        temporada = anime_data['temporada']       
    )
    
    db.session.add(novo_anime)
    db.session.commit()
    
    response = make_response(
        json.dumps({  
            'mensagem': 'Anime cadastrado com sucesso.',  
            'anime': novo_anime.json()  
        },ensure_ascii=False, sort_keys=False)  
    )
    response.headers['Content-Type'] = 'application/json'
    return response

def update_anime(anime_id, anime_data):
    funcionario = Anime.query.get(anime_id)
 
    if not Anime:
        response = make_response(
            json.dumps({'Mensagem':'Anime não encontrado'}, ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response
   
    if not all(key in anime_data for key in ['titulo','genero','estudio', 'temporada']):
        response = make_response(
            json.dumps({'mensagem': 'dados inválidos.Titulo, genero, estudio e temporada são obrigatórios'},ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response
   
    anime.titulo = anime_data['titulo']
    anime.genero= anime_data['genero']
    anime.estudio = anime_data['estudio']
    anime.temporada = anime_data['temporada']
 
    db.session.commit()
 
    response = make_response(
        json.dumps({
            'mensagem':'Anime atualizado com sucesso.',
            'anime': anime.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response

def delete_anime(anime_id):
    confirmarcao = request.args.get('confirmacao')
    
    if confirmarcao != 'True': # se for confirmado
        response = make_response(
            json.dumps({'mensagem': 'confirmacao necessaria para excluir o anime'}, ensure_ascii=False),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response
        
    anime = Anime.query.get(anime_id)
    if not anime:
        response = make_response(
            json.dumps({
                'mensagem': 'Anime não encontrado'
            }, ensure_ascii=False),
            404  
        )
        response.header['Content-Type'] = 'application/json'
        return response
    
    db.session.delete(anime)
    db.session.commit()
    
    response = make_response(
        json.dumps({
            'mensagem': 'Anime excluido com sucesso'
        }, ensure_ascii=False,sort_keys=False)
    )
    response.header['Content-Type'] = 'application/json'
    return response
    
    