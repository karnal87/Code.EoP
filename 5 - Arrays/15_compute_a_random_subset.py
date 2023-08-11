#!/usr/bin/python3

''' PROBLEM
    Write a program that takes as input a positive integer n and a size k <= n, and returns a size k subset
    of {0,1,2,. ..,n - 1}. The subset should be represented as an array. All subsets should be equally
    likely and, in addition, all permutations of elements of the array should be equally likely. You may
    assume you have a function which takes as input a non-negative integer t and returns an integer in
    the set {0,1,.. .,t - 1} with uniform probability.
'''

''' HINT:
        Simulate solution 5.12, using an appropriate data structure to reduce space.
'''

#1 SOLUTION 5.12
# Space: O(1) Time: O(k)
import random
def random_sampling (k, A) :
    for i in range(k):
        # Generate a random index in [i, len(A) - 1]
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]

''' BRUTE FORCE SOLUTION
    Iteratively choose random numbers between 0 and n-1 until we get k distinct values.
    => suffers from performance degradation when k is close to n and requires O(k) additional space
'''

''' OPTIMIZE SOLUTION
    Mimic offline sampling algorithm with A[i] = i, stopping after k iterations.
    => O(n) space and time to create array. 
    => after creating (0,1,2,...,n-1), need O(k) time to produce the subset

    When k << n, most of array untouched. 
    Key to reducing space complexity to O(k) is by simulating A with a hash table.
    Do this by only tracking entries whose values are modified by the algorithm, keeping
    the remainder with a default value.

    Maintain a hash table H whose keys and values are from {0, 1, ..., n-1}.
    H will track the entries touched in the randomization process--these
    entries *may* not be A[i] = i
        * i is in H, then its value is stored at A[i] in the ***brute force*** algorithm
        * if i is not in H, then this implicitly implies A[i] = i

    Since no more than k entries will be tracked, when k is small compared to n, time and
    space will be saved over the brute force solution, which initializes and updates an array
    of length n.
'''

''' SAMPLE PROCESS
    
    Initially, H is empty. Perform k iterations of the following.
    * Choose a random integer r in [0,n-1-i], where i is the current iteration count, starting from 0.
        - Four possibilities, corresponding to whether the two entries in A that are being swapped
          are already present or not present in H. The desired result is in A[0,k-1], which can be 
          determined from H.
EXAMPLE:

    * n = 100, k = 4

    - First iteration:
        * choose a random number -> 28
        * update H[0] = 28, H[28] = 28
            => A[0] is 28 and A[28] is 0 for all other i => A[i] = i
    - Second iteration:
        * choose a random number -> 42
        * update H[1] = 42, H[42] = 1
            => (0,28),(28,0),(1,42),(42,1)
    - Third iteration:
        * choose a random number -> 28 => (a collision!)
        * update H
            => (0,28),(28,2),(1,42),(42,1), (2,0)
    - Fourth iteration:
        * choose a random number -> 64
        * update H
            => (0,28),(28,2),(1,42),(42,1), (2,0), (3,64),(64,3)
    
          
'''

# T: O(k), O(k)
def random_subset(n,k):
    changed_elements = {}
    for i in range(k):
        # Generate a random index between i and n - 1, inclusive
        rand_idx                   = random.randrange(i,n)
        rand_idx_mapped            = changed_elements.get( rand_idx, rand_idx)
        i_mapped                   = changed_elements.get(i,i)
        changed_elements[rand_idx] = i_mapped
        changed_elements[i]        = rand_idx_mapped
    return [ changed_elements[i] for i in range(k) ]

