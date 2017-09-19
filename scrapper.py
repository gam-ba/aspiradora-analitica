import json
import requests
import pandas as pd

def get_comments(signatures, petition_id):
    '''
    Input:
    signature = un diccionario vacío.
    petition_id = número o nombre de la petición.
    
    Output:
    Un diccionario con cuatro pares de keys-values:
    num_comments = número total de comentarios levantados.
    comments_list = una lista de strings con un string por comentario.
    likes = una lista de ints con los likes de cada comentario.
    date = una lista de strings con las fechas -- Ojo! La api lo devuelve medio sucio.
    '''
    last_page = False
    n_items = 0
    idx = 10
    comments = []
    likes = []
    date = []    
    while not last_page:
        comments_url = "https://www.change.org/api-proxy/-/petitions/%s/comments?limit=10&offset=%d&order_by=voting_score" % (str(petition_id), idx)
        comments_json = json.loads(requests.get(comments_url).content)
        if "items" in comments_json:
            n_items += len(comments_json["items"])
            for item in comments_json["items"]:
                comments.append(item["comment"])
                likes.append(item["likes"])
                date.append(item["created_at"])
            last_page = comments_json["last_page"]
            idx += 10
    signatures["num_comments"] = n_items
    signatures["comments_list"] = comments
    signatures["likes"] = likes
    signatures["date"] = date

    return signatures
    
signatures = {}
petition_id = 0

get_comments(signatures, petition_id)
