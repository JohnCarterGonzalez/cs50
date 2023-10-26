#!/usr/bin/env python3

"""
Recursion
    - the process of defining something in terms of itself
    - how one could iterate over lists while avoiding stateful loops
"""
def sum(nums):
    # reached the end of the list and stop the recursion and return 0
    # base case, is the part of the function that does not call itself
    # w/out a recursive fn would call it self forever
    if len(nums) == 0:
        return 0

    # add the first number to the sum of the rest of the numbers
    # recurse, we need to actually call the fn again, but with a smaller input, call
    # sum() with the rest of the numbers i the list [1:]
    return nums[0] + sum(nums[1:])


# factorials recursive v non-recursive
# non-recurse
import functools

def mul(x, y):
    return x, y

def factorials(n):
    return functools.reduce(mul, range(1, n + 1)) if n else 1

# recurse
def factorials(n):
    return n * factorials(n - 1) if n else 1
