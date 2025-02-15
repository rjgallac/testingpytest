from modules import module1, module2, module3, module4



def main_prog():
    test = module1.func1("rob")
    test2 = module2.func2("rob")
    pokes = module3.getpokes()
    people = module4.do_db_stuff()
    return "success: pokes: " + str(len(pokes)) + " people:" + str(len(people))

if __name__ == "__main__":
    main_prog()