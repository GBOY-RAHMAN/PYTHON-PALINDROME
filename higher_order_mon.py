'''
We learned about functions but there is so much more to it!


Here are some funcion attributes we need to go over today


1. Functions in python can be treated as objects
2. Functions can take another funciton as a parameter
3. A Function can chose to return a function 
4. We can create functions much more quickly in python with something called a LAMBA EXPRESSION

'''



'''
Higher order functions are functions that either take another function as a parameter

or return a function as thier result


Higher order funcitons are used to : manipulate data  (data cleaning/filtering)

'''


# What are common higher order functions

def square(n):
    return n * n

numbers = [1, 2, 3, 4, 5]


squares = list(map(square, numbers))  # the map function returns an object not a list, we need to convert


print(squares) # Output: [1, 4, 9, 16, 25]



'''
The filter() function constructs a list from elements of an iterable 
for which a function
returns true



The syntax is: filter(function, iterable)

A filter function can only work with "predicate"

predicate functions are functions that can only return true or false




'''

def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5]

evens = list(filter(is_even, numbers)) # the filter function returns an object not a list, we need to convert

print(evens) # Output: [2, 4]



'''
The reduce() function applies a binary function (a function that takes two arguments) to the
items of an iterable in a cumulative way. This function is not a built-in function and needs
to be imported from the functools module.

'''


from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]



total = reduce(add, numbers)
print(total) # Output: 15


'''

these 3 functions are not the only higher order functions out there...


feel free to research the :

Sorted,


'''



'''
A lambda function in Python is an anonymous function, or a function without a name. These
functions are throw-away functions and are used where they are needed. lambda functions
are used along with built-in functions like filter(), map() and reduce().


lambda arguments: expression

'''


'''
We use a lambda function to quickly define throw away methods
'''

def adder(param1,param2):
    return param1+param2

# use lambda


function = lambda x,y: x+y 

print(function(4,5))


numbers = [1, 2, 3, 4, 5]


squares = list(map(lambda n: n * n , numbers))
print(squares) # Output: [1, 4, 9, 16, 25]











