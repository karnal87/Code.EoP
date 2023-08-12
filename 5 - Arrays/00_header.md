[Home](../README.md)
# General
    * retrieval/update : T: O(1)
    * insertion: resizing considerations
    * deletion at index i := shift everything right of i left => T: O(n-i)
# Array boot camp
```python
    def even_odd(x):
        next_even, next_odd = 0, len(A) - 1
        while next_even < next_odd:
            if A[next_even] % 2 == 0:
                next_even += 1
            else:
                A[next_even], a[next_odd] = a[next_odd], a[next_even]
                next_odd -= 1
```
* noteworthy:
    - brute-force solutions typically use O(n) space, with subtle solutions to use array to reduce space complexity to O(1)
    - filling array tends slower with front-based insertions--opt to write values to end
    - consider overwriting for deletions
    - when dealing with integers, consider processing digits from back; consider reversing with consideration to digit significance
    - be cautious with regards to making off-by-1 errors
    - don't worry about integrity of array unless it's being returned, and then primarily consider at time of return
    - arrays can serve as suitable data structures when the distribution or elements is known in advance or limited
    - when operating with 2-dimensional arrays, use **parallel logic** for rows and columns
    - can be easier to **simulate the specification** than to solve for the general result; 
        * e.g., rather than writing a formula for an i-th entry in order, compute from beginning 
# Know the libraries!
* syntax for instantiation:
    ```python
    l = [1]
    l = [1,2,3]
    l = [1] + [5] # [1,5]
    l = [1] * 5   # [1,1,1,1,1]
    l = list(range(5))   # [0,1,2,3,4]
    ```
* checking if value is in array:
    ```python
    l = [1,2]
    2 in l
    ```
* instantiate a 2-D array:
    ``` python
    l = [ [1,2], [3,4] ]
    l = [ [1]. [5] ]
    ```
* understand how copy works
```python
A = [1,2]
B = A
C = list(A)
```

* key list methods
    ```python
    # TODO:
    ```
* slicing
    ```python
    ```
* list comprehensions
    ```python
    [ x**2 for x in range(10) if x % 2 == 0] # create a list of the first 5 even square numbers
    ```
# 5 Arrays
## 5.1 [The Dutch national flag problem](./01_dutch_national_flag.py)
    * time: O(n) space: O(1)
        - ideal solution: maintain 4 sub-arrays within input array; in relation to pivot
            * less than
            * equal to
            * unclassified
            * greater than
        - all elements start out as unclassified; iterate through elements, moving into either bottom, middle, or top ( $<, ==, >$ )
### Variants
#### Given array of n object with keys that take one of four values, re-order the array so that all objects that have the same key appear together.
#### Given an array A of n objects with Boolean-valued keys, reorder the array so that objects that have the same key appear together. O(1) space and O(n) time
#### Given an array A of n objects with Boolean-valued keys, reorder the array so that objects that have the key false appear first. The relative ordering of objects with key true should not change. Use O(1) s, O(n) t.

## 5.2 [Increment an Arbitrary-Precision Integer](./02_increment_number.py)
    * BRUTE FORCE: convert into integer, increment, convert back to array of digits
    * IMPROVED SOLUTION:
        - operate directly on digits
        - add from left; carry over if applicable, if a[0] == 10 => a[0] = 1, a.append(0)
### VARIANTS
#### Write a program which takes as input two strings s and t of bits encoding binary numbers $B_s + B_t$
## 5.3 [Multiply two arbitrary-precision integers](./03_multiply_number.py)
    * multiply first number by each digit of second number starting from the left
        - better to incrementally add the terms to save space
    * iteration process:
        - r = [0] * (len(x)+len(y))
        - double reverse loop (i,j)
            * r[i+j+1] += x[i] * y[j]
            * r[i+j] += r[i+j+1] // 10
            * r[i+j+1] %= 10
    * O(nm) time O(nm) space
## 5.4 [Advancing through an array](./04_advance_array.py)
    * record: {furthest_can_reach (fcr), last_index (li), len(A)-1}
    * iterate through array while $i <= fcr and fcr < li$
        - fcr = max( fcr, A[i])
        - i++
    * t: O(n), s: O(1)
### Write a program to compute the minimum number of steps needed to advance to the last location.
## 5.5 [Delete duplicates from sorted arrays](./05_delete_dupes.py)
    * BRUTE FORCE: iterate through i, test A[i] == A[i+1] and left shift if condition met; worst-case: O(n^2)
    * IMPROVED: reduce amount of shifting
        - keep a `write_index` to track shifts
            * index starts one-ahead
            * iteration starts at zero
            * write_index is 'written' and incremented when A[write_index] != A[i] 
        - t: O(n), s: O(1)
### Implement a function which takes as input an array and a key, and updates the array so that all occurrences of the input key have been removed and the remaining elements have been shifted left to fill the emptied indices. Return the number of remaining elements. There are no requirements as to the values stored beyond the last valid element.
### Write a program which takes as input a sorted array A of integers and a positive integer m, and updates A so that it x appears m times in A it appears exactly min(2,m) times in A. The update to A should be performed in one pass, and no additional storage may be allocated.
## 5.6 [Buy and sell a stock once](./06_buy_and_sell_stock_once.py)
    * track: local min (price_min_so_far), max_profit  => min_price_so_far = infinity; max_profit = 0y
    * iterate through prices
        - max_profit_today = price - min_price_so_far
        - max_profit       = max(max_profit, max_profit_today)
        - min_price_so_far = min(min_price_so_far, price)
### Write a program that takes an array of integers and finds the length of a longest sub-array all of whose entries are equal.
## 5.7 [Buy and sell a stock twice](./07_buy_and_sell_stock_twice.py)
    * (t,s)O(n), O(n)
    * make array of max forward profit for each day
        * iterate and create forward profit; first_buy_sell_profits = []
            - (i,price) in prices
                * min_price_so_far = min(min_price_so_far, price)
                * max_total_profit = max( max_total_profit, price - min_price_so_far)
                * first_buy_sell_profits[i]
    * find the max profit if we make a second buy
        * iterate in reverse
            - (i, price)  $<- prices[1:], 1$
                * max_price_so_far = max( max_price_so_far, price)
                * max_total_profit = max( max_total_profit, max_price_so_far - price + first_buy_sell_profits[i-1] )
### Solve the same problem in O(n) time and O(1) space.
## 5.8 [Computing an alternation](./08_compute_alternation.py)
* O( n log(n) ) solutions:
    * simplistic solution: sort array, then interleave the bottom and top halves of the sorted array
    * another    solution: sort array, then swap elements in pairs ( A[1], A[2]), ( A[3], A[4] )
* better solution -- rearrange the elements around the median (O(n) (11.8)
* better solution: desired ordering is local 
    $\Rightarrow can simply iterate through array, 
        swapping A[i] and A[i+1] when i is even and A[i] > A[i+1]
        or i is odd and A[i] < A[i+1]$
    ```python   
    # TERSE
    for i in range( len(A)):
        A[i:i+2] = sorted( A[i:i+2], reverse=i % 2)

    # EXPANDED
    for i in range( len(A) ):
        if i % 2 == 0 and A[i] > A[i+1]:
            t = A[i]
            A[i] = A[i+1]
            A[i+1] = t
        elif i % 2 != 0 and A[i] < A[i+1]:
            t = A[i]
            A[i] = A[i+1]
            A[i+1] = t
    ```

## 5.9 [Enumerate all primes to n](./09_enumerate_all_primes.py)
* BRUTE FORCE: iterate over all i from 2 to n; test if prime, add if so
    - $O(n^3/^2)$
    - use "trial division" $\Rightarrow $ divide i by each integer from 2 to $\sqrt(i)$
* IMPROVED: 'sieve' encountered prime numbers
    * $O((n^3/^2)/(log(n))^2$
```python
primes = []
is_prime = [False,False] + [True] * (n-1)
for p in range(2, n+1):
    if is_prime[p]:
        primes.append(p)
        for i in range(p, n+1, p):
            is_prime[i] = False
return primes
```
* FURTHER IMPROVEMENT: use $p^2 as well$
```python
size     = ( n - 3 ) // 2 + 1
primes   = [2]
is_prime = [True] * size
for i in range(size):
    if is_prime[i]:
        p = i * 2 + 3
        primes.append(p)
        for j in range(2 * i**2 + 6 * i + 3, size, p):
            is_prime[j] = False
return primes
```
## 5.10 [Permute the elements of an array](./10_permute_elements.py)
### Given an array A of integers representing a permutation, update A to represent the inverse permutation using only constant additional storage.
## 5.11 [Compute the next permutation](./11_compute_next_permutation.py)
## 5.12 [Sample offline data](./12_sample_offline_data.py)
    - Variant: The rand() function in the standard C library returns a uniformly random number in [0, RAND_MAX - 1]. Does rand() mod n generate a number uniformly distributed in [0, n - 1]?
## 5.13 [Sample online data](./13_sample_online_data.py)
## 5.14 [Compute a random permutation](./14_compute_a_random_permutation.py)
## 5.15 [Compute a random subset](./15_compute_a_random_subset.py)
## 5.16 [Generate nonuniform random numbers](./16_generate_non_uniform_random_numbers.py)
    * Given a random number generator that produces values in [0,1] uniformly, how would you generate a value X from T according to a continuous probability distribution, such as the exponential distribution?
## 5.17 [The Sudoku checker problem](./17_sudoku_checker.py)
## 5.18 [Compute the spiral ordering of a 2D array](./18_compute_spiral_ordering_of_2d_array.py)
    * Given a sequence of integers P, computer a 2D array A whose spiral order is P. (Assume the size of P is $n^2$ 
      for some integer n.)
    * Write a program to enumerate the first *n* pairs of integers ($a$,$b$) in spiral order, starting from
        (0,0) followed by (1,0). For example, if n = 10, your output should be (0,0), (1,0), (1,-1),
        (-1,0),(-1,1),(0,1),(0,1),(1,1),(2,1)
    * Compute the spiral order for an m x m 2D array A.
    * Compute the last element in spiral order for an m x m 2D array A in O(1) time.
    * Compute the kth element in spiral order for an m x n 2D array i O(1) time.
## 5.19 [Rotate a 2D array](./19_rotate_2d_array.py)
    * Implement an algorithm to reflect A, assumed to be an n x n 2D array, about the horizontal axis of symmetry.
      Repeat the same for reflections about the vertical axis, the diagonal from top-left to bottom-right, and the 
      diagonal from top-right to bottom-left.
## 5.20 [Compute rows in Pascals Triangle](./20_compute_rows_in_pascals_triangle.py)
    * Compute the nth row of Pascal's triangle using O(n) space
