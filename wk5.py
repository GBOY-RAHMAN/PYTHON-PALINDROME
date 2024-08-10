#map functions
def square(n):
    return n * n
numbers = [1,2,3,4,5]

squares = list(map(square,numbers))
print(squares)

# filter function
# the filter function only work with predicate and return either true 

def is_even(n):
    return n % 2 == 0
numbers =[1,2,3,4,5]
evens = list(filter(is_even, numbers))
print(evens)#
'''
'''