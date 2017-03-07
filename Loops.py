
'''-------------------------------------------------------------
#------>@author----------->U.Sajid
#Loops programming assignment in python 3
#5 loops in total
 #loop one: print all evens from 2 to 100
 #loop two:print all squares from 1 to 100
 #loop three: print all the powers of 2 from 2^0 to 2^20
 #loop four: odds between a and b, a and b from user inputs
 #loop five: parse odds from a given integer and add

#Loops run in single program seperated by two line
---------------------------------------------------------------------- '''

print("starting program one: even from 2 to a hundred")
print()
#loop one: all evens 2 to a huned
a=0
for i in range(2, 101, 2):
    a+=i
print("the sum of evens from 2 to 100 is: ", a)
print()
print()
print("starting program two: sum of squares 1 to a hundred")
print()
#loop two: sum of squares 1 to a huned
total=0
for i in range(1,101):
    total+=(i**2)
print("sum of squares from 1 to 100 is:", total)

print()
print()
print("starting program three: powers of 2")
print()
#loop three: powers of 2 from 2^0 to 2^20
a=0
for i in range(0,21):
    a=(2**i)
    print("2 to the power {i} is:".format(i=i), a)
print()
print()
#endloop
print("starting program four: odds in range start to end")
print()
#loop four:
a=input("please input a start value: ")
b=input("please enter an end value: ")
result=0
#there is a check to see if the start value entered is even or odd
if int(a)%2==0:
	for i in range(int(a)+1, int(b)+1, 2):
		result+=i
else:
	for i in range(int(a), int(b)+1, 2):
		result+=i
print("the result of all odds between start and end is:", result)
print()
print()
print("starting program five: parse and add odds from integer")
#loop five: parse string to get odds, add odds
a=input("please enter a value: ")
str(a)
result=0
for character in a:
    if(int(character)%2!=0):
        result+=int(character)
    else:
        continue
print("the sum of the odd in the value inserted is:", result)
