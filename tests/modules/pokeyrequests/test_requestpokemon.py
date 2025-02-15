from  modules.pokeyrequests import requestpokemon



def test_get_pokes_request(mocker):
    
    mock_response = mocker.MagicMock()
    mock_response.json.return_value = "{}"
    mocker.patch("requests.get", return_value=mock_response)

    assert requestpokemon.get_pokes_request() == "{}"