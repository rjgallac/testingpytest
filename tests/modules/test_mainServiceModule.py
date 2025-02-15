from modules import mainServiceModule

def test_module1_func1(mocker):
    mocker.patch("modules.whatsUpModule.func2", return_value="pikachu")
    mocker.patch("modules.pokesModule.getpokes", return_value="pikachu")
    mocker.patch("modules.dbModule.do_db_stuff", return_value="pikachu")

    assert mainServiceModule.func1("rob") == "7 people:7"