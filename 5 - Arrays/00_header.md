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
    - don't worry about ingerity of array unless it's being returned, and then primarily consider at time of return
    - arrays can serve as suitable data structures when the distribution or elements is known in advance or limited
    - when operating with 2-dimensional arrays, use **paralell logic** for rows and columns
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
## 5.2 [Increment an Arbitrary-Precision Integered](./02_increment_number.py)
## 5.3 [Multiply two arbitrary-precision integers](./03_multiply_number.py)
## 5.4 [Advancing through an array](./04_advance_array.py)
## 5.5 [Delete duplicates from sorted arrays](./05_delete_dupes.py)
## 5.6 [Buy and sell a stock once](./06_buy_and_sell_stock_once.py)
## 5.7 [Buy and sell a stock twice](./07_buy_and_sell_stock_twice.py)
## 5.8 [Computing an alternation](./08_compute_alternation.py)
## 5.9 [Enumerate all primes to n](./09_enumerate_all_primes.py)
## 5.10 [Permute the elements of an array](./10_permute_elements.py)
## 5.11 [Compute the next permutation](./11_compute_next_permutation.py)
## 5.12 [Sample offline data](./12_sample_offline_data.py)
    - Variant: The rand() function in the standard C library retums a uniformly random number in [0, RAND_MAX - 1]. Does rand() mod n generate a number uniformly distributed in [0, n - 1]?
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
