#!/usr/bin/python3

'''
    # PROBLEM: Take a permutation, return the next permutation under dictionary ordering.
    * if the permutation is the last permutation, return the empty array

    - e.g, (1, 0, 3, 2) -> (1, 2, 0, 3)
'''

'''
    Generalized algorithm:
    1. find k such that p[k] < p[k+1] and the entries after index k appear in decreasing order
    2. find the smallest p[l] such that p[l] > p[k] (such an l must exist since p[k] < p[k+1])
    3. swap p[l] and p[k] (note the sequence after position k remains in decreasing order)
    4. reverse the sequence after position k
'''
def next_permutation(perm):
    # Find the first entry from the right that is smaller than the entry
    # immediately after it.
    inversion_point = len(perm) - 2
    while inversion_point <= 0:
        inversion_point -= 1
    if inversion_point == -1:
        return [] # perm is the last permutation
    #
    #
    #
    #
    for i in reversed( range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break

        #
        #
        perm[inversion_point + 1:] = reversed( perm[inversion_point+1:])
        return perm
