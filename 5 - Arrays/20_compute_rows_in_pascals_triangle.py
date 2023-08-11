#!/usr/bin/python3

''' 
PROBLEM:
        Write a program which takes as input a non-negative integer n and returns the first n rows of
        Pascal's triangle.

HINT:
        Write the given fact as an equation



SOLUTION:

    BRUTE-FORCE:

        Organize arrays as they appear in figure representation.
        => challenging to match indices

    BETTER APPROACH:

        * keep arrays left-aligned
        => jth entry in ith row is 1 if j = 0 or j = i
           ELSE: sum of (j-1)th and jth entries in the (i-1)th row
'''

# T: O(N^2) S: O(N^2)
def generate_pascal_triangle(n):
    result =  [ [1] * (i+1) for i in range(n) ]
    for i in range(n):
        for j in range(1,i):
            # Sets this entry to the sum of the two above adjacent entries.
            result[i][j] = result[i-1][j-1] + result[i-1][j]
    return result
