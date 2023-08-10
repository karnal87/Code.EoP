#!/usr/bin/python

# PROBLEM: Take an array A of n numbers, and rearrangers A's elements to get a new array
#          B having the property that B[0] <= B[1] >= B[2] <= B[3] >= B[4] >= ...

# SOLUTION: Sort A and interleave the bottom and top halves of the sorted array. Alternatively, 
#           could sort A and then swap the elements at the pairs ( A[1], A[2] ),  ( A[3], A[4]), 
#           ... . Both these approaches have the same time complexity as sorting, namely O( n log(n) )


# Time complexity: O(n)
def rearrange(A):
    for i in range(len(A)):
        A[ i : i + 2 ] = sorted( A[ i : i + 2], reverse= i % 2 )
