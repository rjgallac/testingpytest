from main import main_prog
from tests.modules import test_dbModule

def test_answer(mocker):
    mocker.patch("modules.mainServiceModule.func1", return_value="pokes: 7 people:7")

    result = main_prog()
    assert result == "success: pokes: 7 people:7"
