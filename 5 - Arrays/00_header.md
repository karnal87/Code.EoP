# General
    * retrieval/update : T: O(1)
    * insertion: resizing considerations
    * deletion at index i := shift everything right of i left => T: O(n-i)
# Array boot camp
{{{
    def even_odd(x):
        next_even, next_odd = 0, len(A) - 1
        while next_even < next_odd:
            if A[next_even] % 2 == 0:
                next_even += 1
            else:
                A[next_even], a[next_odd] = a[next_odd], a[next_even]
                next_odd -= 1
python}}}
* noteworthy:

# 5 Arrays
## [The Dutch nationl flag problem](./01_dutch_national_flag.py)
