"""
This Python script is for [Assignment 2].

**Author:** Adebowale gbolahan
**Date:** 16-05-2024

**Description:**

**String Manipulation: Palindrome Variants**
1. Check if a given string is a palindrome.
2. Check if a string becomes a palindrome if you can delete one character from it.
3. Given a list of strings, return those strings which are a palindrome.

**Numerical Patterns: Prime Patterns**
1. Check if a given number is prime.
2. Return all prime numbers less than n.
3. Check if two numbers are co-prime (i.e., their greatest common divisor is 1).

**Data Structures: Dictionary Value Retrieval**
1. Given a dictionary, retrieve the value for a given key. If the key doesn't exist, return a
default value.
2. Given a dictionary, find the key with the highest value.
3. Return a list of keys where their corresponding values are above a given threshold.

**Data Structures: Different Structures**
1. Create a data structure of every type that we have learned about today
2. Give a brief description of each in comments (is it mutable/immutable,
sequential/non sequential etc..)

##Algorithm Question##
Write a function that asks a user to input integers to add to a list, when the user is done
adding they will type done. When the user is done adding, take every element in that list and
multiply it by the value of the item in the list before it. If we are at the first value in the list,
then do not do anything When you are done ask the user if they would like to repeat the
process and add new numbers, if yes repeat, if no, print (‘have a nice day!’)

"""


## panlindrome checker ##
print("##checking a word if the user input is a panlindrome or not ##")
print("##_____________________________________________ ##")
print("##exapmle: Civic, MOM ,DADMADAM, PEEP,RADAR, WOW")
print("##_____________________________________________ ##")

def panlindrome_checker ():
   for i in range(3):
     userinput = input('Enter any word to check (or type "exit" to quit): ')

     if userinput.lower() == 'exit':
        print("Exiting the program.")
        break
     reversedinput = userinput[::-1]

     if userinput == reversedinput:
      print(f"'{userinput}' is a palindrome.")
     else:
        print(f"'{userinput}' is not a palindrome.")
panlindrome_checker()
     
# 


# ##
"""
Check if a string becomes a palindrome if you can delete one character from it.
# """
# # def check (user_input = input('Enter any word to check (or type "exit" to quit): ')):
# #   inputreversed = user_input[::-1]
# #   lastword = user_input[:-1]
# #   if lastword == inputreversed:
# #     print("still a palinrome after removing the last word")
# #   else:
# #     print(f"{user_input}Not a palindrome")
# # while True:
# #     user_input = input('Enter any word to check (or type "exit" to quit): ')
# #     if user_input.lower() == "exit":
# #         print("Exiting the program.")
# #         break
# #     check(user_input)


# def find_palindromes(list_string):
  
#   palindromes = []
#   for word in list_string:
#     # Convert the word to lowercase and remove spaces for case-insensitive comparison
#     clean_word = word.lower().replace(" ", "")
#     # Check if the reversed word is equal to the original clean word
#     if clean_word == clean_word[::-1]:
#       palindromes.append(word)
#   return palindromes

# list_string = ["DAD", "MOM", "HOUSE", "BANANA"]
# palindromes = find_palindromes(list_string)
# print(palindromes)  # Output: ['DAD', 'MOM']

#####Numerical Patterns: Prime Patterns****************

# def is_prime(num):
  
#   if num <= 1:
#     return False
#   for i in range(2, int(num**0.5) + 1):
#     if num % i == 0:
#       return False
#   return True


# print(is_prime(8))


# def find_primes(n):
  
#   primes = []
#   for num in range(2, n):
#     if is_prime(num):
#       primes.append(num)
#   return primes

# print(find_primes(9))

#############################################
# def are_coprime(a, b):
  
#   fig = max(1, min(a, b))  # Initialize fig with the smaller number
#   while fig > 1:
#     if a % fig == 0 and b % fig == 0:
#       return False
#     fig = min(a % fig, b % fig)  # Update fig with the remainder of the larger number divided by the smaller remainder
#   return True

# print(are_coprime(6,9))
#############################################################


#####**Data Structures: Dictionary Value Retrieval**##############
# Define the dictionary
# my_dict = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }


# def get_value(dictionary, key, default_value):
#     return dictionary.get(key, default_value)

# # Example 
# key_to_retrieve = "age"
# default_value = "Not Found"

# value = get_value(my_dict, key_to_retrieve, default_value)
# print(f"The value for '{key_to_retrieve}' is: {value}")

# # Trying to retrieve a key that doesn't exist
# key_to_retrieve = "country"
# value = get_value(my_dict, key_to_retrieve, default_value)
# print(f"The value for '{key_to_retrieve}' is: {value}")
#****************************************************************
# def find_max_key(my_dict):
#   """
#   Finds the key with the highest value in a dictionary.

#   :
#       my_dict: The dictionary to search.

#   Returns:
#       The key with the highest value, or None if the dictionary is empty.
#   """
#   if not my_dict:
#     return None
#   max_key = next(iter(my_dict))  # Initialize with any key
#   max_value = my_dict[max_key]
#   for key, value in my_dict.items():
#     if value > max_value:
#       max_key = key
#       max_value = value
#   return max_key

# # Example 
# my_dict = {"apple": 10, "banana": 15, "cherry": 5}
# max_key = find_max_key(my_dict)  # max_key will be "banana"
# #****************************************************************
# def find_keys_above_threshold(my_dict, threshold):
#   """
#   Returns a list of keys where their corresponding values are above a given threshold.

#   Args:
#       my_dict: The dictionary to search.
#       threshold: The value threshold.

#   Returns:
#       A list of keys with values above the threshold.
#   """
#   return [key for key, value in my_dict.items() if value > threshold]

# # Example usage
# my_dict = {"apple": 10, "banana": 15, "cherry": 5}
# keys_above_10 = find_keys_above_threshold(my_dict, 10)  # keys_above_10 will be ["apple", "banana"]


# #******************************Data Structures: Different Structures**********************

# # List: A mutable, ordered (sequential) collection of items.
# # Items can be of different types and can be changed after the list is created.
# my_list = [1, 2, 3, "apple", 5.5]
# print(my_list)
# print("*******************************************")
# # Tuple: An immutable, ordered (sequential) collection of items.
# # Once created, the items in a tuple cannot be changed.
# my_tuple = (1, 2, 3, "apple", 5.5)
# print(my_tuple)
# print("*******************************************")
# # Set: A mutable, unordered (non-sequential) collection of unique items.
# # Does not allow duplicate elements and does not maintain any order.
# my_set = {1, 2, 3, "apple", 5.5}
# print(my_set)
# print("*******************************************")
# # Dictionary: A mutable, unordered (non-sequential) collection of key-value pairs.
# # Keys must be unique and immutable, but values can be of any type and can be changed.
# my_dict = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# print(my_dict)

# print("*******************************************")
# # String: An immutable, ordered (sequential) collection of characters.
# # Strings are used to represent text data and cannot be changed once created.
# my_string = "Hello, World!"
# print(my_string)
# print("*******************************************")

# ##########Algorithm Question4####################################################
# print("***********************Algorithm Question*****************************************")

# def process_list():
#     while True:
#         user_list = []
#         print("Enter integers to add to the list. Type 'done' when finished.")
        
#         # Collecting integers from the user
#         while True:
#             user_input = input("Enter a number (or 'done'): ")
#             if user_input.lower() == 'done':
#                 break
#             try:
#                 number = int(user_input)
#                 user_list.append(number)
#             except ValueError:
#                 print("Please enter a valid integer.")

#         # Multiplying each element by the previous one
#         for i in range(1, len(user_list)):
#             user_list[i] *= user_list[i-1]

#         print("Processed list:", user_list)

#         # Asking if the user wants to repeat the process
#         repeat = input("Would you like to repeat the process and add new numbers? (yes/no): ")
#         if repeat.lower() != 'yes':
#             print("Have a nice day!")
#             break

# # Running the function
# process_list()
