class TokenDesc:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.literal = ''
        self.literal_complete = False
        self.token = None

    def complete(self):
        self.literal_complete = True

    def addLiteralChar(self, char):
        self.literal += char
