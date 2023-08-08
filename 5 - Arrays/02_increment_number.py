#!/usr/bin/python3

# PROBLEM: 
#         Take as input an array of digits encoding a nonnegative decimal integer,
#         increment that, and then convert the resulting value back to an array of
#         digits
#3      For example: (1,2,9) -> (1,3,0)


#4 SOLUTION
#5 BRUCE FORCE: 
# convert convert array into integer, 
def brute_force_increment(A):
    i = str( int( ''.join(A) ) + 1 )
    l = []
    for x in i:
        l.append(x)
    return l
#6 Add one to end, carry forth to beginning if necessary
# TIME:  O(N)
# SPACE: O(1)
def plus_one(A):
    A[-1] += 1
    for i in reversed( range(1, len(A) ) ):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        # there is a carry-out, so we need one more digit to store the result
        # clever: append a 0 at the end of array and update the first entry to 1
        A[0] = 1
        A.append(0)
    return A;
''' 
VARIANT: Write a program which takes as input two strings s, t of bits encoding
         binary numbers B_s, B_t, and returns a new string of bits representing B_s + B_t
'''
# B_s = 0000 0001
# B_t = 0101 0001

