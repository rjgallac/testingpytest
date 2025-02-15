
from modules.pokeyrequests import requestpokemon

def getpokes():
    requests = requestpokemon.get_pokes_request()
    return requests
    # return "pikachu"