from main import main_prog
from modules import module1, module2, module3
from tests.modules import test_module4

def test_answer(mocker):
    mocker.patch("modules.module1.func1", return_value="pikachu")
    mocker.patch("modules.module2.func2", return_value="pikachu")
    mocker.patch("modules.module3.getpokes", return_value="pikachu")
    mocker.patch("modules.db.dbgets.get_db_stuff", return_value="pikachu")

    result = main_prog()
    assert result == "success: pokes: 7 people:7"
