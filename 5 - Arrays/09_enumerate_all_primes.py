#!/usr/bin/python

# PROBLEM: Take an integer, return all the primes between 1 and itself.
#          (Hint: Exclude the multiples of primes.)

# Brute force: iterate all over i from 2 to n. For each i, test if i is prime.
#              ( Divive i by each integer from 2 to the square root of i, ensuring
#                that the remainder is zero. )
# Each test has a O(sqrt(n) ) complexity => O( n * sqrt(n) ) => O(n^(3/2))


# Imrprovement: "Sieve" a prime when it is identified. 

# SOLUTION:

# Give n, return all primes up to and including n.
def generate_primes(n):
    primes = []
    # is_prime[p] represents if p is prime or not. Initially, set each to
    # true, expecting 0 and 1. Then use sieving eliminate nonprimes.
    is_prime = [False, False] + [True] * ( n - 1 )
    for p in range(2, n + 1 ):
        if is_prime[p]:
            primes.append(p)
            # Sieve p's multiples.
            for i in range(p, n + 1, p):
                is_prime[i] = False
    return primes

def generate_primes(n):
    if n < 2:
        return []
    size = ( n - 3) // 2 + 1
    primes = [2] # Stores the primes from 1 to n.
    # is_prime[i] represents ( 2i + 3 )
    # Initially set each to true. Then use sieving to eliminate nonprimes.
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)
            # Sieving from p^2, where p^2 = (4i^2 + 12i + 9). The index is is_prime
            #
            # Note that we need to use long for j because p^2 might overflow.
            for j in range( 2 * i**2 + 6 * i + 3, size, p):
                is_prime[j] = False
    return primes

