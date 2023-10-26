"""
Pure Functions
    - a fn that two properties:
        + always returns the same value given the same arguments
        + its evaluation has no side effects
        + a computational analogue of a mathematical fn
    - are deterministic
    - do not perform an I/O operations
    - do not call any functions that do any of the above
"""
# Pure fn
def findMax(nums):
    max_val = float('-inf')
    for num in nums:
        if max_val < num:
            max_val = num
    return max_val

# Impure fn
global_max = float('-inf')

def findMax(nums):
    for num in nums:
        if global_max < num:
            global_max = num

# Examples
def multiply_by2(nums):
    products = []
    for num in nums:
        products.append(num*2)
    return products

#############

balance = 1000
cars = []

def buy_car(new_car):
    cars.append(new_car)
    balance -= 69

#############

import random

def roll_die(num_sides):
    return random.randint(1, num_sides)



"""
Reference v Value
    - pass by reference: a fn can mutate the original value taht was passed to it
    - pass by value: a fn can not mutate the original value taht was passed into it, it gets a copy
    - in python are passed by reference:
        + lists
        + dictionaries
        + sets
    - these types are passed by value:
        + integers
        + floats
        + strings
        + booleans
        + tuples
    - generally most collection types are passed by reference and most primitives are passed by value
"""

######### Pass by reference (mutable)
def modify_list(lst):
    lst.append(4)
    # my_list = [1, 2, 3, 4]

my_list = [1, 2, 3]
# my_list = [1, 2, 3]
modify_list(my_list)
# my_list = [1, 2, 3, 4]

####### Passed by value (immutable)
def attempt_to_modify(num):
    num += 1

my_num = 1
# my_num = 1
attempt_to_modify(my_num)
# my_num = 1


"""
I/O
    - that parts of a program that interact with the outside world
    - examples of I/O:
        + reading/writing from a file on the hard drive
        + making a network req
        + reading/writing from a db
        + even simply printing to the console
    - sometimes I/O is also called "side effects"
    - I/O needs be contained, a clear location in the code that does the I/O operations
"""

"""
NO-OP
    - if a fn does not return anything, it has side-effects
        + ^ this can also be called 'no-op', or no operation
"""
# Example
def square(x):
    x * x

# this function call makes no sense
square(x)

# useful side-effect (but impure)
y = 5
def add_to(x):
    y += x

# this dn call changes the value of y
# but its impure, and frankly bad code
add_to_y(5)

# the print() fn has side effects, it doesnt return anything, just prints to the console


"""
Assignment

Complete the markdown_to_text function. It's currently a no-op.

It should:

    Remove any # characters that are at the beginning of a line. (headings in markdown)
    Remove any * characters that are at the start or end of a word. (emphasis in markdown)
"""
def remove_characters_from_words(line):
    return ''.join(map(lambda word: word.strip('*#'), list(line))


def markdown_to_text(doc_content):
    return '\n'.join(map(remove_characters_from_words, doc_content.split('\n')))


# Don't edit below this line


def test(doc_content):
    converted_content = markdown_to_text(doc_content)
    print("----------- Original ----------------")
    print(doc_content)
    print("----------- Converted ---------------")
    print(converted_content)
    print("=====================================")


def main():
    test(
        """
# Header 1
This is a *bold statement*
I am #1
This is just plain text. No special markdown.

* This is a list
* lists don't need to change

Well sh*t."""
    )


main()

"""
Memoization
    - caching
    - a specfic type of caching, when you cache (store a copy of) the result of a computation
      so that you dont have to compute it again in the future
    - is always good to memoize?
        + its a tradeoff between memory and speed. if you have a fn thats called often but its very expensive to compute,
          then its probably not worth memoizing b/c you be bloating the amount of RAM your program uses storing the results of the fn
"""


"""
Referential Transparency
    - pure fns are referentially transparent
    - property of a fn taht allows it to be replacsed by its equilvalent output
"""
