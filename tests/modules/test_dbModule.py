from modules import dbModule


def test_module4(mocker):
    mocker.patch("modules.db.dbgets.get_db_stuff", return_value=["pikachu"])
    result = dbModule.do_db_stuff()
    assert result == ["pikachu"]