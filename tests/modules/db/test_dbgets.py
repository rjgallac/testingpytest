from unittest.mock import MagicMock
from modules.db import dbgets



def fetchall():
    return [("Alice", 14), ("Charlie", 34)]

def test_dbgets(mocker):
    expected = [("Alice", 14), ("Charlie", 34)]

    mock_connect = MagicMock()
    mocker.patch('psycopg2.connect', return_value=mock_connect) 
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = expected
    mock_connect.cursor.return_value = mock_cursor   
    
    result = dbgets.get_db_stuff()
    print(result)
    # assert result==[("Alice", 14), ("Charlie", 34)]
    assert result==["Alice", "Charlie"]
