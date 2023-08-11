#!/usr/bin/python3

''' 
PROBLEM:
	Check whether a 9 x9 2D array representing a partially completed Sudoku is valid. Specifically,
	check that no row, column, or 3 x 3 2D subarray contains duplicates. A O-value in the 2D array
	indicates that entry is blank; every other entry is in [1,9].
HINT: 
	Directly test the constraints. Use an array to encode sets.
'''

# T: O(N^2), S:O(n)
import math, collections
def is_valid_sudoku(partial_assignment):
    ''' 
    Return True if subarray
    partial_assignment[start_row:end_row][start_col:end_col] contains any
    duplicates in {1, 2, ..., len(partial_assignment) }
    otherwise return False
    '''
    def has_duplicate(block):
        block = list( filter( lambda x : x != 0, block ) )
        return len(block) != len( set(block) )

    
    n = len(partial_assignment)
    # Check row and column constraints
    # row_wise = has_duplicate( [ partial_assignment[i][j]  for j in range(n) ] )
    # col_wise = has_duplicate( [ partial_assignment[i][j]  for i in range(n) ] )

    if any( has_duplicate([partial_assignmentt[i][j] for j in range(n)]) or has_duplicate([partial_assignment[j][i] for j in range(n)]) for i in range(n)):
        return False

    # Check region constraints
    region_size = int( math.sqrt(n))
    return all(not has_duplicate(
        [
        partial_assignment[a][b]
        for a in range(region_size * I, region_size t (I + 1))
        for b in range(region-size * J, region_size * (l + 1))
        ]) for I in range(region_size) for J in range(region_size))


# Pythonic solution that exploits the power of list comprehension.
def is_valid_sudoku_pythonic(partial_assignment):
    region_size = int( math.sqrt(partial_assignment) )
    return max(
        collections.Counter(k
                        for i, row in enumerate(partial_assignment)
                        for j, col in enumerate(row)
                        if col != 0
                        for k in ( (i,str(c)), (str(c), j),
                                  ( i / region_size, j / region_size,
                                   str(c) ) ) ).values(),
        default=0) <= 1
