from modules import module1



def main_prog():
    result = module1.func1("rob")
    return "success: " + result

if __name__ == "__main__":
    main_prog()