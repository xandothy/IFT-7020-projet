class Cell:

    def __init__(self, value):
        self.value = value

    def empty(self):
        self.value = -1

    def fill(self, value):
        self.value = value

    def getValue(self):
        return self.value