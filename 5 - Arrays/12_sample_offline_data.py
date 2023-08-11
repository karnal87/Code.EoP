#!/usr/bin/python3 
''' PROBLEM:
    Implement an algorithm that takes as input an array of distinct elements and a size, and returns
    a subset of the given size of the array elements. All subsets should be equally likely. Return the
    result in input array itself.

    Let the input array be A, its length n, artd the specified size k.
'''

''' NAIVE
    Iterate through the input array, selecting entries with probability k/n. Although the average number
    of selected entries is k, we may select more or less than k entries in this way
'''
''' NAIVE
    Enumerate all subsets of size k and then select one at random from
    these. Since there are (n choose k) subsets of size k, the time and space complexity are huge. Furthermore,
    enumerating all subsets of size k is nontrivial 

'''

''' OPTIMAL
    * Want to build a subset of exactly size k is to build one of size k-1 and then add
      one more element, selected randomly from the rest.
      - case k = 1: trivial => make one call to random number generator, take returned value mod n 
        ( called r ) and swap A[0] with A[r]
      - case k > 1:  choose one element at random, repeat the same process with the n - 1 element subarray 
                    A[ 1, n - 1 ]; eventually, the random subset occupies the slots A[0, k - 1 ] and the remaining 
                    elements are in the last n - k slots
    
'''

# Space: O(1) Time: O(k)
import random
def random_sampling (k, A) :
    for i in range(k):
        # Generate a random index in [i, len(A) - 1]
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]


''' VARIANT:
    The rand() function in the standard C library retums a uniformly random number in
    [0, RAND_MAX - 1]. Does rand() mod n generate a number uniformly distributed in [0, n - 1]?
'''
