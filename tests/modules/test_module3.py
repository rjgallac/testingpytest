from src.modules import module3

def test_module3(mocker):
    mocker.patch("modules.pokeyrequests.requestpokemon.get_pokes_request", return_value="pikachu")
    assert module3.getpokes() == "pikachu"
