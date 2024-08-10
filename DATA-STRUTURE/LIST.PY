# DATA STRUCTURE IN PYTHON ---- WORKING WITH LIST 

# List-is a built-in data structure used to store an ordered collection of items

# Key Features of Lists:

# Ordered: Lists maintain the order of items as they were added. __You can access elements using their index, which starts at 0.

# Mutable: You can modify the contents of a list after it is created. This includes adding, removing, or changing elements.

# Heterogeneous: Lists can contain elements of different types, such as integers, strings, and even other lists.

# Dynamic: Lists can grow or shrink in size dynamically. You don't need to specify the size when you create a list.

mylist = [1, 2, 3, 4, 5, 6, 'gabriel', [12, 13, 20]]

print("# Initial List")
print(mylist)

print("# Insert method takes 2 arguments, the index value and the item")
mylist.insert(3, 'mark')
print(mylist)

print("# Append method adds an item to the end of the list")
mylist.append('doctor')
print(mylist)

print("# Extend method adds all elements of an iterable")
mylist.extend(['gabriel','gabriel','gabriel'])
print(mylist)

print("# Remove method removes the first occurrence of the item")
mylist.remove('mark')
print(mylist)

print("# Pop method removes and returns the item at the specified index")
item = mylist.pop(6)
print(item)
print(mylist)

print("# Index method returns the index of the first occurrence of the item")
index = mylist.index(3)
print(index)

print("# Count method returns the number of occurrences of the item")
count = mylist.count(1)
print(count)

print("# Sort method sorts the items of the list in place")
mylist = [5, 3, 6, 1, 4, 2]
mylist.sort()
print(mylist)

print("# Reverse method reverses the order of items in the list in place")
mylist.reverse()
print(mylist)

print("# Copy method returns a shallow copy of the list")
mylist_copy = mylist.copy()
print(mylist_copy)
