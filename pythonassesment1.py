
#  Write a for loops that access every other item in the list

    # so in a list of  [1,2,3,4,5], only print 1,3,5
list = [1,2,3,4,5]
for i in list :
 if i % 2 != 0:
    print(i)
print("_______________________")

#  do the same thing in #2 but in reverse.. so in a list of  [1,2,3,4,5], only print  5,3,1
for item in range(len(list), -1, -2) :
    print(item)
print("_______________________")

# Bonus challenge

# write a for loop that finds the largest and second largest and smallest and second smallest number in a list 

    # print the largest, second largest, smallest and second smallest items
    # DO NOT USE THE MIN AND MAX FUNCTIONS
    # also switch the positions of the largest with the smallest
challenge_list = [2, 3, 4, 5, 6, 7]

# Initialize the first element of the list
largest = challenge_list[0]


smallest = challenge_list[0]


second_smallest = challenge_list[0]


second_largest =challenge_list[0]


for num in challenge_list[1:]:
    #  largest and second largest
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:  
        second_largest = num
    
    #  smallest and second smallest
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:  
        second_smallest = num

# Printng  the results
print("Largest:", largest)
print("Second Largest:", second_largest)
print("Smallest:", smallest)
print("Second Smallest:", second_smallest)


def name(num1,num2):
    return num1/num2
name(4,2)
