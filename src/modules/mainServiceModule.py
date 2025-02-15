from modules import whatsUpModule
from modules import pokesModule
from modules import dbModule

def func1(param1):
    pokes = pokesModule.getpokes()
    test2 = whatsUpModule.func2(param1)
    people = dbModule.do_db_stuff()
    return str(len(pokes)) + " people:" + str(len(people))