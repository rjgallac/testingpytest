from modules.db import dbgets

def do_db_stuff():
    names = dbgets.get_db_stuff()
    return names