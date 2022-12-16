# This is a sample Python script.
import random
import numpy as np
from Board import Board

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

win_condition  = 2048
size = 4
moves = []
number_of_simulation = 40
search_length = 30

random.seed(69420132)

for i in range(100000):
    moves.append(random.randint(0, 3))

def print_move_name_by_index(move):
    if move == 0:
        print("LEFT")
    elif move == 1:
        print("RIGHT")
    elif move == 2:
        print("DOWN")
    elif move == 3:
        print("UP")

def is_Win(board):
    if win_condition == -1:
        return False

    if board.highScore == win_condition:
        return True
    else:
        return False

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
    first_move_scores = np.zeros(4)
    for first_move_index in range(4):
        board_with_first_move, first_move_made, first_move_score = Board(size, board).moveCell(first_move_index)
        if first_move_made:
            first_move_scores[first_move_index] += first_move_score
        else:
            continue
        for p in range(number_of_simulation):
            move_number = 1
            search_bord = Board(size, board_with_first_move)
            is_valid = True
            while is_valid and move_number < search_length:
                search_bord, is_valid, score = search_bord.moveRandom()
                if is_valid:

                    first_move_scores[first_move_index] += score
                    move_number += 1
    best_move_index = np.argmax(first_move_scores)
    search_bord, is_valid, score = board.moveCell(best_move_index)
    print_move_name_by_index(best_move_index)
    return search_bord, is_valid

def monteCarlo(board):
    move_count = 0
    is_valid = True
    while is_valid:
        move_count += 1
        board, is_valid = monteCarloMove(board, number_of_simulation, search_length)
        if is_Win(board):
            is_valid = False

        board.printCells()
    return board.highScore, move_count






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
    # highscore, moves_counter = board.moveCells(moves)
    highscore, moves_counter = monteCarlo(board)

    print("Game over! You made it to: " + str(highscore) + " in " + str(moves_counter) + " moves.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
