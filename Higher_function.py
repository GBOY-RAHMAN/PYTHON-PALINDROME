# A lambda function in Python is an anonymous function, or a function without a name. These
# functions are throw-away functions and are used where they are needed. lambda functions
# are used along with built-in functions like filter(), map() and reduce().


# map: Applies a function to all items in an input list.
def mutiply(x):
    return x * x

num = [1,2,3,4,5,6]

data = list(filter(mutiply,num))
print(data)

# filter:Constructs a list from those elements of the input list for which the function returns True.

# reduce: Applies a function of two arguments cumulatively to the items of a sequence.

# Higher-order functions, 
# such as map, filter, reduce, 
# and decorators, are powerful tools in 
# Python for creating abstract and reusable code constructs.