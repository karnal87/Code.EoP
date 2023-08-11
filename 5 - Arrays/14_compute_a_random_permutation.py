#!/usr/bin/python3

''' PROBLEM
	Design an algorithm that creates uniformly random permutations of [0, 1,.. .,n - 1]. You are given
	a random number generator that returns integers in the set {0,1, . . . ,n - 1} with equal probability;
	use as few calls to it as possible.
'''

''' BRUTE FORCE SOLUTION
	Iteratively pick random numbers between 0 and n-1, inclusive. If a number repeats, discard it, repeat.
	Hash table good choice to store and test values that have already been picked.
	=> Space Complexity : O(n) from hash table spillover
	=> Time Complexity: O(n log(n) ) => Coupon Collector's Problem
'''


''' IMPROVED SOLUTION
	* Key is to avoid repeats. 
	So, restrict the set that's randomly chosen from. Apply an offline data type of solution. 
	With (0,1,2,...,n-1) and k = n, partition a partial permutation with the remaining values.
'''
''' EXAMPLE CASE
	n = 4
	Begin with (0,1,2,3)
	- Randomly choose from [0,3] and get 1.
	=> (swap A[0] and A[1]) (i,r) (0,1)
	Have (1,0,2,3)
	- Randomly choose from [1,3] and get 3
	=> (swap A[1] and A[3]) (i,r) (1,3)
	Have (1,3,2,0)
	- Randomly choose from [2,3] and get 3
	=> (swap A[2] and A[3]) (i,r) (2,3)
	Have (1,3,2,0), the final result
'''

# 5.12 solution
# Space: O(1) Time: O(k)
import random
def random_sampling (k, A) :
	for i in range(k):
		# Generate a random index in [i, len(A) - 1]
		r = random.randint(i, len(A) - 1)
		A[i], A[r] = A[r], A[i]


# T: O(n), S: O(1)
def compute_random_permutation (n) :
	permutation = list(range(n))
	random_sampling (n, permutation)
	return permutation 
