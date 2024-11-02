class JsonPost:

    def __init__(self, filename):
        self.filename = filename

    def parsehtml(self, htmlcontent):

        for line in htmlcontent:
            print(line)