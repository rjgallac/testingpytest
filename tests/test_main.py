from main import main_prog
from modules import module1, module2, module3
from tests.modules import test_module4

def test_answer(mocker):
    mocker.patch("modules.module1.func1", return_value="pokes: 7 people:7")

    result = main_prog()
    assert result == "success: pokes: 7 people:7"
