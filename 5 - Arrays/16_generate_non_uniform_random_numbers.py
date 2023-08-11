'''PROBLEM:
	You are given r numbers as well as probabilities po, pt, ... ,pn-r, which sum up to l.
	Given a random number generator that produces values in [0, 1) uniformly, how would you generate one 
	of the n numbers according to the specified probabilities?
'''
''' Hint: 
          Look at the graph of the probability that the selected number is less than or equal to a. What do the
            jumps correspond to?
'''

''' SOLUTION
    
    Partition the unit interval [0,1] into n disjoint segments, in a way such that the length of the 
    jth interval is proportional to p_j.

    Then select a number uniformly at random in the unit interval [0,1] and return the number 
    corresponding tot he interval to the interval the randomly generated number falls in.

    To create these intervals, use { p0, p0 + p1, p0 + p1 + p2, ..., p1 + p2 + ... pn-1 } as endpoints

    For example, using:
    
        3 -> 9 / 18
        5 -> 6 / 18
        7 -> 2 / 18
        9 -> 1 / 18

        ->

        [0.0,0.5), [0.5,0.833), [0.833, 0.944), [0.944,1]


    Using the above example, take a RNG number generated in the interval [0.0, 1.0] is .873
    
    .873 in [0.833,0.944) => 7

IN GENERAL:

    Searching an array of n disjoint intervals for the interval containing a number takes O(n) time.

    HOWEVER, since the array ( p0, p0+p1, p0+p1+p2, .., p0 + p1 + p2 + ... + pn-1) is sorted, binary
    search is an option to find the interval in O(log(n)





'''
# T: O(n) S: O(n) -- for creation, subsequent generations using this will take O(log(n))
import itertools,  bisect, random
def nonnuiform_random_number_generation(values, probabilities):
    prefix_sum_of_probabilities = list( itertools.accumulate(probabilities) )
    interval_idx = bisect.bisect( prefix_sum_of_probabilities, random.random() )
    return values[interval_idx]


''' VARIANT
    Given a random number generator that produces values in [0,1] uniformly, how would
    you generate a value X from T according to a continuous probability distribution, such as the
    exponential distribution?
'''
