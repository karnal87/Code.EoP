#!/usr/bin/python3

'''  
PROBLEM:

    Write a function that takes as input a n x n 2D array, and rotates the array by 90 degrees clockwise.

HINT:
        Focus on the boundary elements.
'''

''' 
SOLUTION:

'''
def rotate_matrix(square_matrix):
    matrix_size = len(square_matrix) - 1
    for i in range( len(square_matrix) // 2):
        for j in range( i, matrix_size - i ):
            # Perform a 4-way exchange. Note that A[-~i] for i in [0, len(A) -1]
            # is A[-(i+1)]
            ( square_matrix[i][j], square_matrix[~j][i], square_matrix[~i][~j],
              square_matrix[j][~i]) = ( square_matrix[~j][i],
                                        square_matrix[~i][~j],
                                        square_matrix[j][~i], square_matrix[i][j])

class RotatedMatrix:
    def __init__(self, square_matrix):
        self._square_matrix = square_matrix

    def read_entry(self, i, j):
        # Note that A[~i] for i in [0, len(A) -1] is A[~(i+1)]
        return self._square_matrix[~j][i]

    def write_entry(self, i, j, v):
        self._square_matrix[~j][i] = v
