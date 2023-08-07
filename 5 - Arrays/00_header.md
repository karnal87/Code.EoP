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


        ```
    * instantiate a 2-D array:

        ``` python
            l = [ [1,2], [3,4] ]
            l = [ [1]. [5] ]
        ```
# 5 Arrays
## 5.1 [The Dutch nationl flag problem](./01_dutch_national_flag.py)
## 5.2 [Increment an Arbitrary-Precision Integered](./02_increment_number.py)
