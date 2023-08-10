#!/usr/bin/python3
# PROBLEM: Write a program taking a sorted array that deletes repeated elements.

# naive solution: S: O(1) T: O(N^2)
# - iterate through A, testing if A[i] == A[i+1] and so on, shifting from A[i+2] onwards to the left
#   when all elements are equal, the # of shifts is: (n-1) + (n-2) + ... + 2 + 1 => n^2 => O(n^2)
 
# SOLUTION: 
# T: O(N); S: O(1)
def delete_duplicates(A):
    if not A: return
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index


'''
Variant: Implement a function which takes as input an array and a key, and updates the array so
    that all occurrences of the input key have been removed and the remaining elements have been
    shifted left to fill the emptied indices. Return the number of remaining elements. There are no
    requirements as to the values stored beyond the last valid element.

Variant: Write a program which takes as input a sorted atay A of integers and a positiveinteger m,
    and updates A so that if x appears z times in A it appears exactly mn(Z,m) times in A. The update
    to A should be performed in one pass, and no additional storage may be allocated.
'''
