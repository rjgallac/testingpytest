from modules import mainServiceModule



def main_prog():
    result = mainServiceModule.func1("rob")
    return "success: " + result

if __name__ == "__main__":
    main_prog()