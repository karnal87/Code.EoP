# Problem: take an array of n integers, where A[i] := the maximum you can advance from index i
#          return whether it is possible to advance to the last index starting from the 
#          beginning of the array

# Time Complexity: O(n) ; Space Complexity: O(1)
def can_reach_end(A):
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index

''' 
Variant: 
        Write a program to compute the minimum number of steps needed to advance to the last
        location.
'''
