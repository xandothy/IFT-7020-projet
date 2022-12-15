from Cell import Cell


class Board:

    def __init__(self, size):
        self.size = size
        self.cells = self.generateCells()

    def generateCells(self):
        cells = []
        for column in range(self.size):
            columns = []
            for row in range(self.size):
                columns.append(Cell(-1))
            cells.append(columns)
        return cells

    def setCell(self, column, row, value):
        cell = self.cells[column][row]
        if cell.value == -1:
            cell.fill(value)
            return True
        else:
            return False

    def printCells(self):
        values = []
        for i in range(self.size):
            rowValues = []
            for j in range(self.size):
                rowValues.append(self.cells[i][j].value)
            values.append(rowValues)
        for i in values:
            print(i)

    def moveCells(self, moves):
        for move in moves:
            if move == 0:
                self.left()
            elif move == 1:
                self.right()
            elif move == 2:
                self.down()
            elif move == 3:
                self.up()
            self.printCells()

    def left(self):
        possible = False
        for i in range(self.size):
            for j in range(self.size - 1):
                ##print(self.cells[i][j].value)
                ##print(self.cells[i][j-1].value)
                if self.cells[i][j].value == self.cells[i][j + 1].value and self.cells[i][j+1].value != -1:
                    self.cells[i][j].fill(self.cells[i][j+1].value * 2)
                    self.cells[i][j+1].empty()
                    possible = True
                elif self.cells[i][j].value == -1 and self.cells[i][j+1].value != -1:
                    self.cells[i][j].fill(self.cells[i][j+1].value)
                    self.cells[i][j+1].empty()
                    possible = True
        if possible == False:
            print("this move won't do anything")

    def right(self):
        possible = False
        for i in range(self.size):
            for j in range(self.size -1):
                ##print(self.cells[i][j].value)
                ##print(self.cells[i][j-1].value)
                if self.cells[i][j].value == self.cells[i][j + 1].value and self.cells[i][j].value != -1:
                    self.cells[i][j + 1].fill(self.cells[i][j].value * 2)
                    self.cells[i][j].empty()
                    possible = True
                elif self.cells[i][j + 1].value == -1 and self.cells[i][j].value != -1:
                    self.cells[i][j + 1].fill(self.cells[i][j].value)
                    self.cells[i][j].empty()
                    possible = True
        if possible == False:
            print("this move won't do anything")

    def down(self):
        possible = False
        for j in reversed(range(self.size)):
            for i in (range(self.size-1)):
                ##print(self.cells[i][j].value)
                ##print(self.cells[i][j-1].value)
                if self.cells[i][j].value == self.cells[i+1][j].value and self.cells[i][j].value != -1:
                    self.cells[i+1][j].fill(self.cells[i][j].value * 2)
                    self.cells[i][j].empty()
                    possible = True
                elif self.cells[i+1][j].value == -1 and self.cells[i][j].value != -1:
                    self.cells[i+1][j].fill(self.cells[i][j].value)
                    self.cells[i][j].empty()
                    possible = True
        if possible == False:
            print("this move won't do anything")

    def up(self):
        possible = False
        ##this looks at column by column
        for j in range(self.size):
            for i in (range(self.size -1)):
                print(self.cells[i][j].value)
                print(self.cells[i+1][j].value)
                if self.cells[i][j].value == self.cells[i+1][j].value and self.cells[i][j].value != -1:
                    self.cells[i][j].fill(self.cells[i+1][j].value * 2)
                    self.cells[i+1][j].empty()
                    possible = True
                elif self.cells[i][j].value == -1 and self.cells[i+1][j].value != -1:
                    self.cells[i][j].fill(self.cells[i+1][j].value)
                    self.cells[i+1][j].empty()
                    possible = True
        if possible == False:
            print("this move won't do anything")
