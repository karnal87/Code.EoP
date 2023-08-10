
# PROBLEM: Given an array A of n elements and a permutation P, apply P to A. 

# HINT: Any permutation can be viewed as a set of cyclic permutations. For an element in
#       a cycle, how would you identify if it has been permuted?

# Simple solution: Allocate additional storage then map B[P[i]] = A[i] for each A, then map B to A. 
# => T: O(n), S: O(n)

# key insight for reducing space complexity: decompose permutations into simpler structures, then process 
#                                            incrementally
# e.g. (a,b,c,d) ->
# (d) -> 0
# (c) -> 1
# (b) -> 2
# (a) -> 3
# => (d,c,b,a)

# method to perform similar operations while using constant storage: sign bit entries in the permutation array
# (3,1,2,0) -> 
# P[0]: 3 -> 0 => 
#       A[0] -> A[3]
#       t = A[3] => (-1,1,2,0)
#       A[3] -> A[0]
#       P[0] < 0 => cycle starting at 0 done
#                   (-1,1,2,-4)
# P[1]: 1 -> 1
#       ...

def apply_permutation(perm, A):
    for i in range(len(A)):
        # Check if the element at index i has not been moved by checking if
        # perm[i] is nonnegative
        n = i
        while perm[n] >= 0:
            A[i], A[perm[n]] = A[perm[n]], A[i]
            temp = perm[n]
            # Subtracts len(perm) from an entry in perm to make it negative,
            # which indicates the corresponding move has been performed.
            perm[n] -= len(perm)
            n        = temp
    # Restore perm.
    perm[:] = [ a + len(perm) for a in perm ]



# if cannot use the sign bit, allocate an array of n Booleans, indicating whether
# an element has been processed.
def apply_permutation(perm, A):
    def cyclic_permutation(start, perm, A):
        i, temp = start, A[start]
        while True:
            next_i    = perm[i]
            next_temp = A[next_i]
            A[next_i] = temp
            i, temp = next_i, next_temp
            if i == start: break

    for i in range( len(A) ):
        # Traverses the cycle to see if i is the minimum element. 
        j = perm[i]
        while j != i:
            if j < i: break
            j = perm[j]
        else:
            cyclic_permutation(i, perm, A)

''' 
Variant: Given an array A of integers representing a permutation, update A to represent the inverse
    permutation using only constant additional storage.
'''
