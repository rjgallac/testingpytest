from modules import pokesModule

def test_pokesModule(mocker):
    mocker.patch("modules.pokeyrequests.requestpokemon.get_pokes_request", return_value="pikachu")
    assert pokesModule.getpokes() == "pikachu"
