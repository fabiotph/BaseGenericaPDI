from src.FileHandler import FileHandler


class Tokenizer:
    def __init__(self):
        super().__init__()
        self.n_token = 0
        self.typeMatrix = None
        self.col = None
        self.row = None
        self.data = []

    def tokenize(self, fileHandler=None, fileName=""):
        reader = fileHandler
        if reader is None:
            reader = FileHandler(fileName)
        line = reader.read_next_line()
        while line:
            if line[0] is "#":
                line = reader.read_next_line()
                continue
            tokens = line.split(" ")
            for token in tokens:
                self.set_token(token)
            line = reader.read_next_line()

    def set_token(self, value):
        value = value.rstrip("\n")
        value = value.replace(" ", "")
        if value == '':
            return
        limit = (2, 3)[self.typeMatrix == 'P2']
        if self.n_token > limit:
            self.data.append(int(value))
        else:
            if self.n_token == 0:
                self.typeMatrix = value
            elif self.n_token == 1:
                self.row = int(value)
            elif self.n_token == 2:
                self.col = int(value)
            self.n_token += 1
