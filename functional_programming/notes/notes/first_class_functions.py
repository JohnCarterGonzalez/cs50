"""
Anonymous Functions
    - have no name, also called lambda functions
"""
lambda x: x + 1

# this is a function that takes a single arg 'x' and returns 'x + 1', you can assign it to variable and call it like any other function

add_one = lambda x: x + 1
print(add_one(2))
# 3

# you can create functions on the fly and pass them around as data

def categorize_file(filename):
    # ?

    return get_category(filename[filename.rfind(".") :])


# Don't edit below this line

"""
Assignment

Complete the categorize_file function. It should take in a single argument, filename, and return a string representing the category of the file. The categories are as follows:

    Text if the file ends with .txt
    Document if the file ends with .docx
    Code if the file ends with .py
    Unknown if the file ends with anything else

The last line of the function is already written for you. It does the heavy lifting of parsing the extension out of the filename. You just need to write the logic for determining the category.

The last line expects an anonymous get_category function to exist. You should create that function using a lambda expression. It should take in a single argument, extension, and return a string representing the category of the file.

Tip:
The built-in dictionaries .get method might help to implement this.
"""
def categorize_file(filename):
    get_category = {
        ".txt" => "Text",
        ".docx" => "Document",
        ".py" => "Code"
    }.get(extension, "Unknown")


    return get_category(filename[filename.rfind(".") :])

def test(filename):
    category = categorize_file(filename)
    print(f"The file {filename} is of type {category}")


def main():
    files = [
        "document1.txt",
        "notes.docx",
        "essay.docx",
        "bot.py",
        "unknown.xyz",
    ]

    for file in files:
        test(file)


main()


"""
First Class and higher order functions
    - functions in that language are treated like any other variable
        + first class function: a fn that is treated like any other value
        + higher order function: a fn that accepts another fn as an arg or returns a fn
"""
# First class example
def square(x):
    return x * x

f = square

print(f(5))
# 25

# Higher Order functions
def square(x):
    return x * x

def my_map(fn, arg_list):
    result = []
    for i in arg_list:
        result.append(fn(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)

# [1, 4, 9, 16, 25]

"""
Map
    - "map", "filter", "reduce", are commonly used in fn programming
    - the built-in "map" fn takes a fn and an iterable( eg. a list ) and returns a new iterable where the fn has been applied to each element
"""
def square(x):
    return x * x

nums = [1, 2, 3, 4]
squared_nums = map(square, nums)
print(squared_nums)

"""
Filter
    - takes a fn and an iterable, returns a new iterable that only contains elements from the original iterable
      where the result on the item returned True
"""
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)
# [2, 4, 6]

"""
Reduce
    - fn that takes a fn and a list of values and applies the fn to each value in the list, accumulating a result as it goes
"""
import functools

def add(sum, y):
    return sum + y

numbers = [1, 2, 3, 4, 5]

accum = functools.reduce(add, numbers) # add is the fn, sum is the accum, numbers is the list of values
print(accum)
# 15

"""
How do map, filter, and reduce help with fp?
"""
# imperative example:
def factorial(n):
    # a procedure that continuously multiplies
    # the current result by the next number
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# a higher order fn like reduce will alow us to rm the stateful iteration and mutate of the result variable
import functools

def mul(x, y):
    return x * y

def factorial(n):
    return functools.reduce(mul, range(1, n + 1))
