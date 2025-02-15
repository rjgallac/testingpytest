from modules import module2
from modules import module3
from modules import module4

def func1(param1):
    pokes = module3.getpokes()
    test2 = module2.func2(param1)
    people = module4.do_db_stuff()
    return str(len(pokes)) + " people:" + str(len(people))