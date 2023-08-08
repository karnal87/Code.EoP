#!/usr/bin/python3

# e.g.: 123, 987
#   7   * 123       = 861
#   123 *   8 * 10  = 9840
#   99  * 123 * 100 = 110700

# time complexity: O(mn), m, n := # of digits for each multipler
def multiply_digit(s,t):
    sign = -1 if (s[0] < 0) ^ (t[0] < 0) else 1
    s[0], t[0] = abs(s[0]), abs(t[0])

    result = [0] * ( len(s) + len(t) )
    for i in reversed( range(len(s) ) ):
        for j in reversed( range( len(t) ) ):
            result[i+j+1] += s[i] + t[j]
            result[i+j]   += result[i+j+1] // 10
            result[i+j+1] %= 10

    # Remove the leading zeroes
    result = result[ next( (i for i, x in enumerate(result) if x != 0 ), len(result)): ] or [0]
    return [ sign * result[0] ] + result[1:]
