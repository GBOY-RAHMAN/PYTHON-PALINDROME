print("Hello world")

#  this is a single line comments


'''
a
a
a
a
a
a

'''



'''
Different variables in python

int = this is a whole number
float = this is a decimal number
boolean = a value of true or false
char = this is a single character string
string = this is anything in quotations that is not a char


some facts about the datatypes

   1. Boolean can only be assigned the values  True or False 
    the T and F must be capitalised or else python will crash

   2.  We use single quotes like this '' to denote a char, and " " to denote string
       however unlike java c++ etc.. you will not crash your code if you create a char with ""

 you can convert variables to other variables through "casting" .. we will visit this later







How to create variables in python...


there are some rules

1. variable name cannot begin with a number
2. variable name cannot include special characters
3. variables are case sensitive , meaning num = 4  and Num = 5 are 2 different variables
4. you do not need to specify a type when creating a variable
5. you may include an underscore in your variable name

'''


num = 7
Num = 8


NUM = 9  # if your variable name is in all caps, this means it is a constant variable

# a constant variable is a variable whos value is not allowed to change


print(num)
print(Num)


'''
printing in python 

we use the keyword print

if you would like to print multiple variables in one print statement

you need to seperate them using commas

this looks like :

print(var1,var2,var3)

the comma adds a space between them... if you do not want this space, then you will use a 


you may also combine text with variables by seperating them with commas

'''

print("hello, my fave num is",num)
print("hello, my fave num is",num,"my friends fave num is",Num)

'''
if statements in python

they follow the following syntax 




if(condition):
    #this code will run



IMPORTANT Side note :    

In python we do not use brackets anywhere....

instead of using brackets to denote what is in a function or in an if statement
or in a loop

we will use INDENTATION

in order to signify to python that a block of code is inside 

a function or in an if statement or in a loop, we MUST use indentation

an indent is just a tab








python has the following comparison operators 

== this means equal to
!= this means not equal to
<  this means less than
>  this means greater than
<= this means less than or equal to
>= this means greater than or equal to


python has the following logical operators :

and  
or
not



Lets create some if statements

'''
a = 10
b = 5 
c = 100


if (a>7 and b <=10): 
    print("yaaay")

    if (100 >10):
        print('this is also indented')
    

# BRACKETS MATTER

if(a>3 and (b<10 or 8==10)):

    print("woah")






# the not operator will just negate the truth value of a boolean statement or value

sunny = False

if (not(sunny)):
    print("it is cloudy")


# accept user input!  

# we will use the input() function to accept an input from a user

# usually the code will look like this :

value = input("Hello user, what is your name? ")

print("hello",value,"it is nice to meet you!")


'''
Arrays in python 

Arrays in python are not called arrays, they are called lists....

why does it have a diff name?

Lists in python behave differently than ARRAYs

1. You can store diferrent variable types within one list in python :O


you create a list like so :

'''

mylist = [1,3,10,"Hello",False,3.14]

# list indexing is the same as arrays.. 

# to access a specific item in a list, we will use its index.. this looks like :


# lets say I want to print first item

print(mylist[0])


# lets say print 4th item?

print(mylist[3])

# how to print the number of items in a list?  we use the len()

print(len(mylist))  # this is going to be useful in many different examples in the future.



# Python allows for negative indexing :O

print(mylist[-1])  # this prints the last item


# there are 4 main functions you will use frequently with lists.
'''

    1. len() - prints the number of items in the list
    2. append(value) - adds a value to the END of the list
    3. pop(index) - removes an item at the specified index
    4. insert(index,value) - inserts an item into the list at the speficied value


'''
mylist = [1,2,3]


# add 4 to the end of  mylist... now list is [1,2,3,4]

mylist.append(4)


# remove the second item in mylist  [1,3,4]

mylist.pop(1)

# insert the value 5 at the 3rd position   [1,3,5,4]

mylist.insert(2,5)
print(mylist)


'''
loops in python 

the main ones are 

while and for 

when to use wich?


we will always use while loops when we do not know how many times we plan to loop

this is because a while loop can go infinitely as long as the condition does not become false


for loops are used to parse through data structures such as strings, lists and much more...




A while loop looks and behaves just like an if statement only istead of running the block once
while loops will keep repeating the block until the condition becomes false


'''

num = 0

complete = False


while(num<10):
    print(num)
    num +=1


newlist = []

while(complete == False):
    resp = input("hello user, give me a number to add to a list, type 0 to exit")
    if resp == '0':
        complete = True
        print("ok byebye")
    else:
        newlist.append(resp)
        print(newlist)



newnum = newlist[0] / newlist[1]
