from Parser import Parser


class Checker:

    def __init__(self):
        parser = Parser()
        for element in parser.check_status():
            print('New test failed: ' + element)

    # global ARTIFACT_ID
    # ARTIFACT_ID = 144070184


Checker()



