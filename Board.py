from random import random, randint, seed
import copy as c
import numpy as np
from Cell import Cell

seed(694201337)
np.random.seed(694201337)


class Board:

    def __init__(self, size, copy=None):
        if copy is None:
            self.size = size
            self.cells = self.generateCells()
            self.highScore = 0
        else:
            self.size = copy.size
            self.cells = c.deepcopy(copy.cells)
            self.highScore = c.deepcopy(copy.highScore)


    def has_empty_cells(self):
        for i in range(self.size):  # line
            for j in range(self.size):  # col
                if self.cells[i][j].getValue() == -1:
                    return True

        return False

    def randomNumber(self):
        column = randint(0, self.size - 1)
        row = randint(0, self.size - 1)
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

    def addNewRandomTiles(self):

        column, row, value = self.randomNumber()
        filleable = self.setCell(column, row, value)
        while not filleable:
            column2, row2, value2 = self.randomNumber()
            filleable = self.setCell(column2, row2, value2)

    def moveRandom(self):
        move_made = False
        move_order = [0, 1, 2, 3]
        while not move_made and len(move_order) > 0:
            move_index = np.random.randint(0, len(move_order))
            move = move_order[move_index]
            board, move_made, score = self.moveCell(move)
            if move_made:
                if not self.has_empty_cells():
                    break

                return board, True, score
            move_order.pop(move_index)
        return board, False, score

    def moveCell(self, move):
        is_moved = False
        if move == 0:
            possible = self.left()
            if possible:
                self.addNewRandomTiles()
                is_moved = True

        elif move == 1:
            possible = self.right()
            if possible:
                self.addNewRandomTiles()
                is_moved = True

        elif move == 2:
            possible = self.down()
            if possible:
                self.addNewRandomTiles()
                is_moved = True

        elif move == 3:
            possible = self.up()
            if possible:
                self.addNewRandomTiles()
                is_moved = True

        for i in range(self.size):  # line
            for j in range(self.size):  # col
                self.cells[i][j].setMergeable(True)

        return self, is_moved, self.highScore

    def moveCells(self, moves):
        moves_done = []
        moves_counter = 0

        for move in moves:
            if move == 0:
                possible = self.left()
                if possible:
                    moves_counter += 1
                    self.addNewRandomTiles()
                else:
                    if 0 not in moves_done:
                        moves_done.append(0)
            elif move == 1:
                possible = self.right()
                if possible:
                    moves_counter += 1
                    self.addNewRandomTiles()
                else:
                    if 1 not in moves_done:
                        moves_done.append(1)
            elif move == 2:
                possible = self.down()
                if possible:
                    moves_counter += 1
                    self.addNewRandomTiles()
                else:
                    if 2 not in moves_done:
                        moves_done.append(2)
            elif move == 3:
                possible = self.up()
                if possible:
                    moves_counter += 1
                    self.addNewRandomTiles()
                else:
                    if 3 not in moves_done:
                        moves_done.append(3)

            moves_done.sort()

            if [0, 1, 2, 3] == moves_done:
                return self.highScore, moves_counter

            for i in range(self.size):  # line
                for j in range(self.size):  # col
                    self.cells[i][j].setMergeable(True)

            self.printCells()
            print("\n")
        return self.highScore, moves_counter

    def left(self):
        # print("LEFT")
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
                    elif cell.getValue() != self.cells[i][j - k].getValue() and self.cells[i][
                        j - k].getValue() == -1:  # move
                        self.cells[i][j - k].fill(cell.getValue())
                        self.cells[i][j - k + 1].empty()
                        possible = True
                    elif not self.cells[i][j - k].getMergeable():
                        wall = True
                    elif cell.getValue() == self.cells[i][j - k].getValue() and cell != self.cells[i][j - k]:  # merge
                        self.cells[i][j - k].fill(cell.getValue() * 2)
                        self.cells[i][j - k + 1].empty()
                        self.cells[i][j - k].setMergeable(False)
                        if self.cells[i][j - k].value > self.highScore:
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

        # if not possible:
        #     print("this move won't do anything")
        return possible

    def right(self):
        # print("RIGHT")
        possible = False
        for i in range(self.size):
            for j in range(self.size - 1, -1, -1):
                wall = False
                cell = self.cells[i][j]
                k = 1  # col

                while not wall:
                    if cell.getValue() == -1:  # La cell n'a pas à bouger
                        wall = True
                    elif j + k - 1 == self.size - 1:  # On est sur le bord du board
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
                        if self.cells[i][j + k].value > self.highScore:
                            self.highScore = self.cells[i][j + k].value
                        possible = True

                    if j + k <= self.size - 1:
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
        # if not possible:
        #     print("this move won't do anything")
        return possible

    def down(self):
        # print("DOWN")
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
                        if self.cells[i + k][j].value > self.highScore:
                            self.highScore = self.cells[i + k][j].value
                        possible = True

                    if i + k <= self.size - 1:
                        cell = self.cells[i + k][j]
                    k += 1

        # if not possible:
        #     print("this move won't do anything")
        return possible

    def up(self):
        # print("UP")
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
        # if not possible:
        #     print("this move won't do anything")
        return possible
