from random import random, randint, seed

from Cell import Cell

seed(694201337)

class Board:

    def __init__(self, size):
        self.size = size
        self.cells = self.generateCells()
        self.highScore = 0

    def randomNumber(self):
        column = randint(0, self.size-1)
        row = randint(0, self.size-1)
        value = 0
        generator = random()
        if generator < 0.9:
            value = 2
        else:
            value = 4
        return column, row, value

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
                possible = self.left()
                if(possible):
                    column, row, value = self.randomNumber()
                    filleable = self.setCell(column, row, value)
                    while (filleable == False):
                        column2, row2, value2 = self.randomNumber()
                        filleable = self.setCell(column2, row2, value2)
            elif move == 1:
                possible = self.right()
                if (possible):
                    column, row, value = self.randomNumber()
                    filleable = self.setCell(column, row, value)
                    while (filleable == False):
                        column2, row2, value2 = self.randomNumber()
                        filleable = self.setCell(column2, row2, value2)

            elif move == 2:
                possible = self.down()
                if (possible):
                    column, row, value = self.randomNumber()
                    filleable = self.setCell(column, row, value)
                    while (filleable == False):
                        column2, row2, value2 = self.randomNumber()
                        filleable = self.setCell(column2, row2, value2)
            elif move == 3:
                possible = self.up()
                if (possible):
                    column, row, value = self.randomNumber()
                    filleable = self.setCell(column, row, value)
                    while (filleable == False):
                        column2, row2, value2 = self.randomNumber()
                        filleable = self.setCell(column2, row2, value2)

            for i in range(self.size):  # line
                for j in range(self.size):  # col
                    self.cells[i][j].setMergeable(True)

            self.printCells()
            print("\n")
        return self.highScore

    def left(self):
        print("LEFT")
        possible = False
        for i in range(self.size):  # line
            for j in range(self.size):  # col
                wall = False
                cell = self.cells[i][j]
                k = 1  # col

                while not wall:
                    if cell.getValue() == -1:  # La cell n'a pas à bouger
                        wall = True
                    elif j - k + 1 == 0:  # On est sur le bord du board
                        wall = True
                    elif cell.getValue() != self.cells[i][j-k].getValue() and self.cells[i][j-k].getValue() == -1:  # move
                        self.cells[i][j-k].fill(cell.getValue())
                        self.cells[i][j-k+1].empty()
                        possible = True
                    elif not self.cells[i][j-k].getMergeable():
                        wall = True
                    elif cell.getValue() == self.cells[i][j-k].getValue() and cell != self.cells[i][j-k]:  # merge
                        self.cells[i][j-k].fill(cell.getValue()*2)
                        self.cells[i][j-k+1].empty()
                        self.cells[i][j-k].setMergeable(False)
                        if (self.cells[i][j - k].value) > self.highScore:
                            self.highScore = self.cells[i][j - k].value
                        possible = True

                    cell = self.cells[i][j - k]
                    k += 1


                    """
                    if self.cells[i][j].value == self.cells[i][j + 1].value and self.cells[i][j+1].value != -1:
                        self.cells[i][j].fill(self.cells[i][j+1].value * 2)
                        self.cells[i][j+1].empty()
                        if (self.cells[i][j+1].value) > self.highScore:
                            self.highScore = self.cells[i][j+1].value
                        possible = True
                    elif self.cells[i][j].value == -1 and self.cells[i][j+1].value != -1:
                        self.cells[i][j].fill(self.cells[i][j+1].value)
                        self.cells[i][j+1].empty()
                        possible = True
                    """

        if possible == False:
            print("this move won't do anything")
        return possible

    def right(self):
        print("RIGHT")
        possible = False
        for i in range(self.size):
            for j in range(self.size-1, -1, -1):
                wall = False
                cell = self.cells[i][j]
                k = 1  # col

                while not wall:
                    if cell.getValue() == -1:  # La cell n'a pas à bouger
                        wall = True
                    elif j + k - 1 == self.size-1:  # On est sur le bord du board
                        wall = True
                    elif cell.getValue() != self.cells[i][j + k].getValue() and self.cells[i][j + k].getValue() == -1:
                        self.cells[i][j + k].fill(cell.getValue())
                        self.cells[i][j + k - 1].empty()
                        possible = True
                    elif not self.cells[i][j + k].getMergeable():
                        wall = True
                    elif cell.getValue() == self.cells[i][j + k].getValue() and cell != self.cells[i][j + k]:
                        self.cells[i][j + k].fill(cell.getValue() * 2)
                        self.cells[i][j + k - 1].empty()
                        self.cells[i][j + k].setMergeable(False)
                        if (self.cells[i][j + k].value) > self.highScore:
                            self.highScore = self.cells[i][j + k].value
                        possible = True

                    if j+k <= self.size-1:
                        cell = self.cells[i][j + k]
                    k += 1

                """
                if self.cells[i][j].value == self.cells[i][j + 1].value and self.cells[i][j].value != -1:
                    self.cells[i][j + 1].fill(self.cells[i][j].value * 2)
                    self.cells[i][j].empty()
                    if (self.cells[i][j-1].value) > self.highScore:
                        self.highScore = self.cells[i][j-1].value
                    possible = True
                elif self.cells[i][j + 1].value == -1 and self.cells[i][j].value != -1:
                    self.cells[i][j + 1].fill(self.cells[i][j].value)
                    self.cells[i][j].empty()
                    possible = True
                """
        if possible == False:
            print("this move won't do anything")
        return possible

    def down(self):
        print("DOWN")
        possible = False
        for j in range(self.size):
            for i in range(self.size - 1, -1, -1):
                wall = False
                cell = self.cells[i][j]
                k = 1  # col

                while not wall:
                    if cell.getValue() == -1:  # La cell n'a pas à bouger
                        wall = True
                    elif i + k - 1 == self.size - 1:  # On est sur le bord du board
                        wall = True
                    elif cell.getValue() != self.cells[i + k][j].getValue() and self.cells[i + k][j].getValue() == -1:
                        self.cells[i + k][j].fill(cell.getValue())
                        self.cells[i + k - 1][j].empty()
                        possible = True
                    elif not self.cells[i + k][j].getMergeable() or not cell.getMergeable():
                        wall = True
                    elif cell.getValue() == self.cells[i + k][j].getValue() and cell != self.cells[i + k][j]:
                        self.cells[i + k][j].fill(cell.getValue() * 2)
                        self.cells[i + k - 1][j].empty()
                        self.cells[i + k][j].setMergeable(False)
                        if (self.cells[i + k][j].value) > self.highScore:
                            self.highScore = self.cells[i + k][j].value
                        possible = True

                    if i + k <= self.size - 1:
                        cell = self.cells[i + k][j]
                    k += 1

        if possible == False:
            print("this move won't do anything")
        return possible

    def up(self):
        print("UP")
        possible = False
        ##this looks at column by column
        for j in range(self.size):
            for i in (range(self.size)):
                wall = False
                cell = self.cells[i][j]
                k = 1  # line

                while not wall:
                    if cell.getValue() == -1:  # La cell n'a pas à bouger
                        wall = True
                    elif i - k + 1 == 0:  # On est sur le bord du board
                        wall = True
                    elif cell.getValue() != self.cells[i - k][j].getValue() and self.cells[i - k][j].getValue() == -1:
                        self.cells[i - k][j].fill(cell.getValue())
                        self.cells[i - k + 1][j].empty()
                        possible = True
                    elif not self.cells[i - k][j].getMergeable():
                        wall = True
                    elif cell.getValue() == self.cells[i - k][j].getValue() and cell != self.cells[i - k][j]:
                        self.cells[i - k][j].fill(cell.getValue() * 2)
                        self.cells[i - k + 1][j].empty()
                        self.cells[i - k][j].setMergeable(False)
                        if (self.cells[i - k][j].value) > self.highScore:
                            self.highScore = self.cells[i - k][j].value

                        possible = True

                    cell = self.cells[i - k][j]
                    k += 1
        if possible == False:
            print("this move won't do anything")
        return possible
