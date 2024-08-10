import math
# Use the filter() function to find all the ages that are:
# 1. Less than 20.
# 2. Between 20 and 40.
# 3. Greater than 40.
def age_lesser(n):
    return n  < 20 
 
def midage(f):
    return f >= 20 and f <= 40
      
    #     return True
    # else:
    #     return False
        
def above(m):
    return m > 40
ages = [15, 22, 34, 40, 65, 18, 23, 30, 45, 50]
lesser_age = list(filter (age_lesser, ages))

print("age lessser than 20")
print(lesser_age)

print("--------------------------")

print("---Age between 20 and 40---")
range_age = list(filter (midage, ages))
print(sorted(range_age))
print("----------above40----------------")
older = list(filter(above,ages))
print(sorted(older))


# Transforming Data with map()
# Using the ages list from above, use map() to:
# 1. Add 5 years to each age.
# 2. Halve each age.
# 3. Convert each age to its square root (you'll need the math module).
 
def adages(add):
    return add + 5
def halfages(half):
    return half/ 2
def squareroot(square):
    return math.sqrt(square)

newagesList = list(map(adages,ages))
print(newagesList)

print("------Half Age-----")

newHalfAge = list(map(halfages,ages))
print(newHalfAge)
   

agesquare  = list(map(squareroot,ages))

print(agesquare)


from functools import reduce
def proage(x,y):
    return x * y


productage = reduce(proage,ages)
print(productage)

def napply(funcs, x):
    for func in funcs:
       x = func(x)
    return x
       

f1 = lambda x: x + 2 
f2 = lambda x: x * 2 
f3 = lambda x: x - 3


print(napply([f1, f2, f3], 5)) # Expected: ((5+2)*2)-3 = 11
    


    
#     def compose(f, g): pass
# Example:
# f = lambda x: x + 2 g = lambda x: x * 3
# h = compose(f, g)
# print(h(3)) # Expected: (3*3)+2 = 11;