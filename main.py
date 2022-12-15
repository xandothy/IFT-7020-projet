# This is a sample Python script.
import random

from Board import Board


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


size = 4
moves = [0, 2, 3, 6, 1, 3, 2, 2, 1, 2, 1, 0, 3, 2, 2, 1, 0, 1, 0, 2, 3, 3, 2]
def randomNumber():
    column = random.randint(0, size-1)
    row = random.randint(0, size-1)
    value = 0
    generator = random.randint(0,1)
    if generator == 0:
        value = 2
    elif generator == 1:
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
