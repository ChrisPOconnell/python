__author__ = 'chris'
def obstructed_vertically_above(a_row, a_col, a_deployment):
    '''
    Precondition 1: a_row and a_col are between 0 and 7
    Precondition 2: a_deployment has form [n0, n1, ..., n7], 0 <= ni <= 7
    meaning that there is a queen in column ni of row i.

    Example: The deployment in the board below is [6,7,2,3,5,4,0,1].
    (It is not a stable deployment.)
    ---0 1 2 3 4 5 6 7
    0--0 0 0 0 0 0 Q 0
    1--0 0 0 0 0 0 0 Q
    2--0 0 Q 0 0 0 0 0
    3--0 0 0 Q 0 0 0 0
    4--0 0 0 0 0 Q T 0
    5--0 F 0 0 Q 0 0 0
    6--Q 0 0 0 0 0 0 0
    7--0 Q 0 0 0 0 0 0

    Returns: obstructed_by_queen_vertically = True only if, and only if
    a_deployment has a queen in column a_col and in a row above a_row
    Example: obstructed_vertically_above(6, 5, d) would return True if d were
    the above board.
    '''

    obstructed_by_queen_vertically = False  # until shown otherwise
    for row_above in range(0, a_row):  # consider every row above a_row
        if a_deployment[row_above] == a_col:  # a is queen in this column
            obstructed_by_queen_vertically = True
            break  # no point is continuing to look
    return obstructed_by_queen_vertically


def obstructed_diagonally_above(a_row, a_col, a_deployment):
    '''
    Preconditions: as for obstructed_vertically_above
    Returns: obstructed_by_queen_diagonally = True only if, and only if
    a_deployment contains a queen diagonally above a_col in rows < a_row,

    Example:   __ __ __ Q
               __ __ __ __  (we'll check (a_row-1, a_col-1) and (a_row-1, a_col+1) etc.)
               __ X  __ __  a_row = 2, a_col = 1
    '''
    obstructed_by_queen_diagonally = False  # until shown otherwise
    for row_above in range(1, a_row + 1):  # consider every row above a_row
        if a_deployment[a_row - row_above] == a_col - row_above:  # a queen up 1 and left 1
            obstructed_by_queen_diagonally = True
            break  # no queen possible in this column; advance to next col_num
        if a_deployment[a_row - row_above] == a_col + row_above:  # a queen up 1 and right 1
            obstructed_by_queen_diagonally = True
            break  # no queen possible in this column; advance to next col_num
    return obstructed_by_queen_diagonally


def obstructed_above(a_row, a_col, a_deployment):
    '''
    Preconditions: as for obstructed_vertically_above
    Returns obstructed = True only if, and only if a_deployment contains a queen
    diagonally or vertically above a_row, a_col
    '''

    obstructed = False
    for queen_index in range(a_row):  # only consider queens above the row
        if obstructed_vertically_above(a_row, a_col, a_deployment):
            obstructed = True; break
        if obstructed_diagonally_above(a_row, a_col, a_deployment):
            obstructed = True; break
    return obstructed


# Test obstructed_vertically_above()
print('\n +++++++++++ TEST RESULT obstructed_vertically_above +++++++++++++++')
print('True<---->' + str(obstructed_vertically_above(7, 4, [5,4])))
test_deployment = (6,7,2,3,5,4,0,1)

#----0 1 2 3 4 5 6 7
# 0--0 0 0 0 0 0 Q 0
# 1--0 0 0 0 0 0 0 Q
# 2--0 0 Q 0 0 0 0 0
# 3--0 0 0 Q 0 0 0 0
# 4--0 0 0 0 0 Q T 0
# 5--0 F 0 0 Q 0 0 0
# 6--Q 0 0 0 0 0 0 0
# 7--0 Q 0 0 0 0 0 0

print(test_deployment)
print ('\nobstructed_vertically_above(4, 6, test_deployment) EXPECT True: ' \
       + str(obstructed_vertically_above(4, 6, test_deployment)))
print ('\nobstructed_vertically_above(5, 1, test_deployment) EXPECT False: ' \
       + str(obstructed_vertically_above(5, 1, test_deployment)))
print ('\nobstructed_vertically_above(7, 7, test_deployment) EXPECT True: ' \
       + str(obstructed_vertically_above(7, 7, test_deployment)))

# Test obstructed_by_queen_diagonally_above()
print('\n +++++++++++ TEST RESULT obstructed_by_queen_diagonally_above +++++++++++++++')
test_deployment = (6,7,2,3,5,4,0,1)

#----0 1 2 3 4 5 6 7
# 0--0 0 0 0 0 0 Q 0
# 1--0 0 0 0 0 0 0 Q
# 2--0 0 Q F T F 0 0
# 3--0 0 0 Q 0 0 0 0
# 4--0 0 0 0 T Q 0 0
# 5--0 0 0 0 Q 0 0 0
# 6--Q 0 0 0 0 0 0 0
# 7--0 Q 0 0 0 0 0 0

print('\n')
print(test_deployment)
print('obstructed_diagonally_above(2,3,test_deployment) EXPECT False: '
    + str(obstructed_diagonally_above(2,3,test_deployment)))
print('obstructed_diagonally_above(2,4,test_deployment) EXPECT True: '
    + str(obstructed_diagonally_above(2,4,test_deployment)))
print('obstructed_diagonally_above(2,5,test_deployment) EXPECT False: '
    + str(obstructed_diagonally_above(2,5,test_deployment)))
print('obstructed_diagonally_above(4,4,test_deployment) EXPECT True: '
    + str(obstructed_diagonally_above(4,4,test_deployment)))
print('obstructed_diagonally_above(4,0,test_deployment) EXPECT True: '
    + str(obstructed_diagonally_above(4,0,test_deployment)))
print('obstructed_diagonally_above(6,7,test_deployment) EXPECT True: '
    + str(obstructed_diagonally_above(6,7,test_deployment)))


# Test obstructed_above()
print('\n +++++++++++ TEST RESULT obstructed_above +++++++++++++++')
deployment = (6,7,2,3,5,4,0,1)

#----0 1 2 3 4 5 6 7
# 0--0 0 0 0 0 0 Q 0
# 1--0 0 0 0 0 0 0 Q
# 2--0 0 Q F 0 0 0 0
# 3--0 0 0 Q 0 0 0 0
# 4--0 0 0 0 0 Q 0 0
# 5--0 T 0 0 Q 0 0 0
# 6--Q 0 0 0 0 0 0 0
# 7--0 Q 0 0 T 0 0 0

print('\n')
print(test_deployment)
print('obstructed_above(2,3,test_deployment) EXPECT False: '
     + str(obstructed_above(2,3,deployment)))
print('obstructed_above(5,1,test_deployment) EXPECT True: '
    + str(obstructed_diagonally_above(5,1,deployment)))
print('obstructed_above(7,4,test_deployment) EXPECT True: '
    + str(obstructed_above(7,4,deployment)))

