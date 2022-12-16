# This is a sample Python script.
import random

from Board import Board


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


size = 8
moves = []

random.seed(694201337)

for i in range(500):
    moves.append(random.randint(0, 3))

def randomNumber():
    column = random.randint(0, size-1)
    row = random.randint(0, size-1)
    value = 0
    generator = random.random()
    if generator < 0.9:
        value = 2
    else:
        value = 4
    return column, row, value


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board(size)
    board.printCells()
    column1, row1, value1 = randomNumber()
    column2, row2, value2 = randomNumber()
    filleable = board.setCell(column1, row1, value1)
    filleable2 = board.setCell(column2, row2, value2)
    print("Filling the board on first try")
    while(filleable2 == False):
        column2, row2, value2 = randomNumber()
        filleable2 = board.setCell(column2, row2, value2)
    board.printCells()
    print("Starting game")
    highscore = board.moveCells(moves)
    print("Game over! You made it to: " + str(highscore))







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
