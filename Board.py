from random import random, randint

from Cell import Cell


class Board:

    def __init__(self, size):
        self.size = size
        self.cells = self.generateCells()
        self.highScore = 0

    def randomNumber(self):
        column = randint(0, 1)
        row = randint(0, 1)
        value = 0
        generator = randint(0, 1)
        if generator == 0:
            value = 2
        elif generator == 1:
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
            self.printCells()
            print("\n")
        return self.highScore

    def left(self):
        print("LEFT")
        possible = False
        for i in range(self.size):
            for j in range(self.size - 1):
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
        if possible == False:
            print("this move won't do anything")
        return possible

    def right(self):
        print("RIGHT")
        possible = False
        for i in range(self.size):
            for j in range(self.size -1):
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
        if possible == False:
            print("this move won't do anything")
        return possible

    def down(self):
        print("DOWN")
        possible = False
        for j in reversed(range(self.size)):
            for i in (range(self.size-1)):
                if self.cells[i][j].value == self.cells[i+1][j].value and self.cells[i][j].value != -1:
                    self.cells[i+1][j].fill(self.cells[i][j].value * 2)
                    self.cells[i][j].empty()
                    if (self.cells[i+1][j].value) > self.highScore:
                        self.highScore = self.cells[i+1][j].value
                    possible = True
                elif self.cells[i+1][j].value == -1 and self.cells[i][j].value != -1:
                    self.cells[i+1][j].fill(self.cells[i][j].value)
                    self.cells[i][j].empty()
                    possible = True
        if possible == False:
            print("this move won't do anything")
        return possible

    def up(self):
        print("UP")
        possible = False
        ##this looks at column by column
        for j in range(self.size):
            for i in (range(self.size -1)):
                if self.cells[i][j].value == self.cells[i+1][j].value and self.cells[i][j].value != -1:
                    self.cells[i][j].fill(self.cells[i+1][j].value * 2)
                    self.cells[i+1][j].empty()
                    if (self.cells[i][j].value) > self.highScore:
                        self.highScore = self.cells[i][j].value
                    possible = True
                elif self.cells[i][j].value == -1 and self.cells[i+1][j].value != -1:
                    self.cells[i][j].fill(self.cells[i+1][j].value)
                    self.cells[i+1][j].empty()
                    possible = True
        if possible == False:
            print("this move won't do anything")
        return possible
