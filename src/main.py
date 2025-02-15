from modules import module1, module2, module3, module4



def main_prog():
    print("Hello World!")
    test = module1.func1("rob")
    print(test)
    test2 = module2.func2("rob")
    print(test2)
    print(module3.getpokes())
    print(module4.do_db_stuff())


if __name__ == "__main__":
    main_prog()