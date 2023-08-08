#!/usr/bin/python3


# with a pivot, partition array so all elements less than pivot appear at the beginning
# USE CASE: to account for worst-case performance (when there are many duplicate elements,
#           causing high deep function call stacks )

# TOY CASE: [0,1,2,0,2,1,1]
#           pivot index: 3 => A[3] = 0
#           => 
#           valid paritionng: [0,0,1,2,2,1,1] 
#           pivot index 2 => A[2] = 2
#           valid paritiong: [0,1,0,1,1,2,2] or [ 0,0,1,1,1,2,2]

# GENERAL PROBLEM: 
#                   Write a program taking an array A and index i into A, that rearranges
#                   the elements such that all the elements less than A[i] (the "pivot")
#                   appear first, followed by the elements equal to the pivot, followed by
#                   the elementws greater than the pivot.


# SOLUTION:
# O(N) space & time approach
#
#                       * form 3 lists, (< pivot, == pivot, > pivot )
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    a, b, c = [], [], []
    for i in range(len(A)):
        x = A[i]
        if x < pivot:
            a.append(x)
        elif x == pivot:
            b.append(x)
        else:
            c.append(x)
    a.extend(b)
    a.extend(c)
    return a

# SOLUTION:
# O(1) space & O(N^2) time approach
#
#                       * iterate through A starting from 0 then 1, and on
#                           - seek an element smaller than pivot, swap as soon as it found
#                       * iterate through A starting from n-1 then n-2, and on
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: group elements < pivot
    for i in range(len(A)):
        # Look for smaller elements
        for j in range(i+1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    # Second pass: group elements > pivot
    for i in reversed( range( len(A) ) ) :
        if A[i] < pivot:
            break
        # Look for a larger element. Stop when we reach an element > pivot
        # , since first pass has moved them to the start of A.
        for j in reversed( range(i) ):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break


# SOLUTION:
# O(1) space & O(N) time approach
#
#                       * make a first pass
#                           - move all elements < pivot to beginning
#                       * make a second pass
#                           - move all elements > pivot to the end
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: group elements < pivot
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    # Second pass: group eleemnts larger than pivot
    larger = len(A) - 1
    for i in reversed( range( len(A) ) ):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # Keep the following invariants during partitioning:
    # - bottom group:       A[:smaller]
    # - middle group:       A[smaller:equal]
    # - unclassified group: A[equal:larger]
    # - top group:          A[larger:]
    smaller, equal, larger  = 0, 0, len(A)
    while equal < larger:
        # A[equal] is the incoming unclassified element.
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else: # A[equal] > pivot
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]

'''
Variant 
Assuming that keys take one of three values, reorder the array so that all objects with the
same key appear together. The order of the subarrays is not important. For example, both Figures
5.1(b) and 5.1(c) on Page 40 are valid answers for Figure 5.1(a) on Page 40. Use O(1) additional
space and O(n) time.

Variant: Given an array A of n objects with keys that takes one of four values, reorder the array so
that all objects that have the same key appear together. Use O(1) additional space and O(n) time.

Variant Given an array A of n objects with Boolean-valued keys, reorder the array so that objects
that have the key false appear first. Use O(1) additional space and O(n) time.

Variant Given em array A of n objects with Boolean-valued keys, reorder the array so that objects
that have the key false appear first. The relative ordering of objects with key true should not change.
Use O(1) additional space and O(n) time.
'''
