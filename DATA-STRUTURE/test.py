currentage = int(input("how old are you "))
def life_in_weeks(age):
    maxYrs = 90
    ageleft =  maxYrs - age
    week = ageleft * 52
    print(f"you have {week} weeks to live")

life_in_weeks(currentage)