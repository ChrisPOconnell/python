__author__ = 'chris'
from eight_queens.obstruction_tests import obstructed_above

BOARD_SIZE = 8

def get_stable_configurations():
    '''
    Intent: Solve the n-queens problem
    Returns: board = BOARD_SIZE queens on BOARD_SIZE x BOARD_SIZE chessboard
    Example: board = [0, 3, 1, 4, 2] for BOARD_SIZE = 5
    '''

    # 1 (Configurations on truncated board):
    # 0 <= row_index <= BOARD_SIZE - - AND stable_configurations =
    # all stable n-queen configurations on an row_index-by-BOARD_SIZE chess board
    # Example: s[3] = [2, 5, 7] means queens at col 2 in row 0, col 5 in row 1 etc.

    row_index = 0
    # Queen of row 0 can be in any column; stable on 0-by-BOARD_SIZE chess board
    stable_configurations = \
            [[0,0,0,0,0,0,0,0], [1,0,0,0,0,0,0,0], [2,0,0,0,0,0,0,0], [3,0,0,0,0,0,0,0], \
            [4,0,0,0,0,0,0,0], [5,0,0,0,0,0,0,0], [6,0,0,0,0,0,0,0], [7,0,0,0,0,0,0,0]]


    # 2 (Complement):  row_index >= BOARD_SIZE - 1

    while row_index < BOARD_SIZE - 1:  # termination fulfills subgoal 3 (see Note 1 below)

             <INSERT CODE HERE FROM SPREADSHEET>

    return stable_configurations

# Note 1: This could have been written as a "for" loop; however,
# writing it as a "while" loop clarifies what it's here for

# TEST
print("------- TEST of get_stable_configurations() -------")
stable_configurations = get_stable_configurations()
print("\nNumber of solutions: " + str(len(stable_configurations)) + "\n")
print(stable_configurations)
