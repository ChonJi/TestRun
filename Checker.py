from Parser import Parser

class Checker(Parser):

    global ARTIFACT_ID
    ARTIFACT_ID = 144070184

    for element in Parser.check_status():
        print('New test failed: ' + element)
