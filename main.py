# This is a sample Python script.
import random
import numpy as np
from Board import Board

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


size = 5
moves = []
number_of_simulation = 40
search_length = 30

random.seed(69420132)

for i in range(100000):
    moves.append(random.randint(0, 3))


def randomNumber():
    column = random.randint(0, size - 1)
    row = random.randint(0, size - 1)
    value = 0
    generator = random.random()
    if generator < 0.9:
        value = 2
    else:
        value = 4
    return column, row, value

def monteCarloMove(board, number_of_simulation, search_length):
    possible_first_moves = [0, 1, 2, 3]
    first_move_scores = np.zeros(4)
    for first_move_index in range(4):
        board_with_first_move, first_move_made, first_move_score = Board(board).moveCells([first_move_index])
        if first_move_made:
            first_move_scores[first_move_index] += first_move_score
        else:
            continue
        for _ in range(number_of_simulation):
            pass
def monteCarlo(board):
    move_count = 0
    is_valid = True
    while is_valid:
        move_count += 1
        board, is_valid = monteCarloMove(board, number_of_simulation, search_length)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board(size, None)
    board.printCells()
    column1, row1, value1 = randomNumber()
    column2, row2, value2 = randomNumber()
    filleable = board.setCell(column1, row1, value1)
    filleable2 = board.setCell(column2, row2, value2)
    print("Filling the board on first try")
    while (filleable2 == False):
        column2, row2, value2 = randomNumber()
        filleable2 = board.setCell(column2, row2, value2)
    board.printCells()
    print("Starting game")
    highscore, moves_counter = board.moveCells(moves)
    print("Game over! You made it to: " + str(highscore) + " in " + str(moves_counter) + " moves.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
