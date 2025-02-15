import requests

def get_pokes_request():
    print("getpokes")
    r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
    return r.json()