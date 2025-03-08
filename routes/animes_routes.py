from flask import Blueprint, request  
from controllers.animes_controllers import(
   get_animes,
   get_anime_by_id,
   get_anime_by_titulo,
   delete_anime,
   create_anime,
   update_anime
)
 
anime_routes = Blueprint('anime_routes', __name__)  
 
@anime_routes.route('/Animes', methods=['GET'])
def anime_get():
    return get_animes()
 
@anime_routes.route('/Anime/<int:anime_id>', methods =['GET'])
def anime_get_by_id(anime_id):
    return get_anime_by_id(anime_id)
 
@anime_routes.route('/Anime/<string:anime_titulo', methods=['GET'])
def anime_get_by_nome(anime_titulo):
   return get_anime_by_titulo(anime_titulo)


@anime_routes.route('/Anime/', methods = ['POST'])
def anime_post():
    return create_anime(request.json)

@anime_routes.route('/Anime/<int:anime_id>', methods = ['PUT'])
def anime_put(anime_id):
    return update_anime(anime_id)

@anime_routes.route('/Anime/<int:anime_id>', methods = ['DELETE'])
def anime_delete(anime_id):
    return delete_anime(anime_id)
