from main import main_prog
from modules import module1, module2, module3, module4

def test_answer(mocker):
    mocker.patch("modules.module1.func1", return_value="pikachu")
    mocker.patch("modules.module2.func2", return_value="pikachu")
    mocker.patch("modules.module3.getpokes", return_value="pikachu")
    mocker.patch("modules.db.dbgets.get_db_stuff", return_value="pikachu")

    main_prog()
