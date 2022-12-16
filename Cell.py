class Cell:

    def __init__(self, value):
        self.value = value
        self.mergeable = True

    def empty(self):
        self.value = -1

    def fill(self, value):
        self.value = value

    def getMergeable(self):
        return self.mergeable

    def setMergeable(self, mergeable):
        self.mergeable = mergeable

    def getValue(self):
        return self.value
