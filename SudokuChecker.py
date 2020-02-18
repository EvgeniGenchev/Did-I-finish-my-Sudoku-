# this program requires numpy lib 
def done_or_not(board):
    import numpy as np
    a = True
    square = np.array(board).reshape((3, 3, 3, 3)).transpose((0, 2, 1, 3)).reshape((9, 9))
    
    for number in range(len(board)):
        a = a and len(set(board[number])) == len(board)
        a = a and len(set(list(map(list, zip(*board)))[number])) == len(board)
        a = a and len(set(square[number])) == len(square[number])
    if a:
        return 'Finished!'
    else:
        return 'Try again!'

#calling the function I pass an example sudoku board
done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8],
             [4, 9, 8, 2, 6, 1, 3, 7, 5],
             [7, 5, 6, 3, 8, 4, 2, 1, 9],
             [6, 4, 3, 1, 5, 8, 7, 9, 2],
             [5, 2, 1, 7, 9, 3, 8, 4, 6],
             [9, 8, 7, 4, 2, 6, 5, 3, 1],
             [2, 1, 4, 9, 3, 5, 6, 8, 7],
             [3, 6, 5, 8, 1, 7, 9, 2, 4],
             [8, 7, 9, 6, 4, 2, 1, 5, 3]])
