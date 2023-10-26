#!/usr/bin/env python3

"""
What is functional programming?
    - paradigm where programs compose functions rather than mutate state( update/setting variables )
    - is declarative, declaring what you want to happen rather than what/how as in imperative
    - functional programming need not mutate the values of any variables, no statefulness
"""
# imperative
num = get_a()
num = transform_a(num)
num = transform_b(num)
return num

# functional
return transform_b(transform_a(get_a()))

"""
Functional v OOP
    - similar to OOP, the core pillars of OOP:
        + encapsulation
        + polymorphism
        + abstraction
        + inheritance
    - the only one that conflicts with fn programming is inheritance
"""


"""
Immutablility
    - a core tenet of fn programming is that data should be immutable, once created, never/cannot be changed
    - immutable data is easier to reason about
    - fewer bugs and more maintable code
"""

"""
Declarative Programming
    - TODO: read more articles on declarative/imperative approach
"""

"""
Its math
    - take the following equation: avg = Σx/N
        + declarative way to writing the average of the numbers in a list x
"""
# in an imperative way
# the state of 'total' is kept tracked/mutated in the process
def get_average(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)

# functional way
# no mutated state
def get_average(nums):
    return sum(nums) / len(nums)

"""
Classes v Functions
    - classes encouragae the dev to think about the world as a series of objects
        + objects bundle behaviour, data, and state together
    - functions encourage the dev the think about the world as a series of transformations of data
        + take data as input, transform it, and return its output
"""
