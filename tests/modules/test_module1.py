from modules import module1

def test_module1_func1(mocker):
    mocker.patch("modules.module2.func2", return_value="pikachu")
    mocker.patch("modules.module3.getpokes", return_value="pikachu")
    mocker.patch("modules.module4.do_db_stuff", return_value="pikachu")

    assert module1.func1("rob") == "7 people:7"