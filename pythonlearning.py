# print("helloword!\n helloword")
# h1="hedaing1"

# name = len(str(input("what is your name?")))

# Bills And Tips caculator python by me gboy
# print("welcome to the tip calculator")
# totalbill= float(input('how much is your total bill ?')) 
# tips=int(input("how much tips will you like to give? 10,12,or 15 ?"))
# share=int(input("how many people to split the biils ?"))
# tax = round((12/100)*totalbill,2)
# sbills = totalbill + tax
# aftertax = round(sbills / share,2)
# aftertips = aftertax + tips

# print(f"okay every total bill is {sbills} plustax {tax} ")
# print(f"after tax is {aftertax}")
# userinput = str(input("will you like  to add the tips yes or no ?"))
# if userinput == "yes":
#     print(f"okay your final bill after tips is {aftertips} ")
# else:
#     print(f"okay every total bill is {sbills} plustax {aftertax} ")
# print("payment method")
# for i in range(share) :
#   print(f"each person will pay {aftertax}")
#   payment = str(input("Kindly complete 1st payment?"))
#   if payment == True: 
#      continue
#   else:
#      print("you need to pay the amout")
# print("complete paymented thank you for shopping with us")
  
# import random
# for i in range(1000000):
#     validchars='abcdefghijklmnopqrstuvwxyz1234567890'
#     loginlen=random.randint(4,15)
#     login=''
#     for i in range(loginlen):
#      pos=random.randint(0,len(validchars)-1)
#      login=login+validchars[pos]
#     if login[0].isnumeric():
#       pos=random.randint(0,len(validchars)-10)
#       login=validchars[pos]+login
#     servers=['@gmail','@yahoo','@redmail','@hotmail','@bing','@outlook']
#     servpos=random.randint(0,len(servers)-1)
#     email=login+servers[servpos]
#     tlds=['.com','.sa','.ng','.in','.net','.org','.qa']
#     tldpos=random.randint(0,len(tlds)-1)
#     email=email+tlds[tldpos]
#     print(email)


# random_int = random.randint(1,5)
# print(random_int)

# import my_module
# import random

# print(my_module.pi)
# random_info = random.random()
# print(round(random_info,2)) 

# my_module.testing_function(fname="2004-10-11",lname="2001-11-4",newdate="2001-05-01")