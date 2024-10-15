import time

def getage1():
    correct = False
    while correct != True:
        try:
            year = int(input("enter your school year 7-13 "))
            if year < 7 or year > 13:
                print("not the correct range\n")
                correct = False
            else:
                correct = True
        except ValueError:
            print("i asked for an integer! \n")
    age = 11 + (year - 7)
    return age

age1 = getage1()
age2 = getage1()
age3 = getage1()
age4 = getage1()
age5 = getage1()

sum = age1 + age2 + age3 + age4 + age5

diff = max(age1, age2, age3, age4, age5) - min(age1, age2, age3, age4, age5)

print( f"The total age is {sum} and the differnce is {diff}")

time.sleep(5)
