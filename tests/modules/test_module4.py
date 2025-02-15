from modules import module4


def test_module4(mocker):
    mocker.patch("modules.db.dbgets.get_db_stuff", return_value=["pikachu"])
    result = module4.do_db_stuff()
    assert result == ["pikachu"]