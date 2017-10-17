''' ----------------------------------------
@author --> Usama S. 

Converter programs 
5 convertor
	#1 -- inches to yards, feet
	#2 -- celsius to fahrenheit
	#3 -- fahrenheit to celsius

--------------------------------------------- '''
import sys
def getNum(inputString):
	try:
		i = float(input(inputString))
	except Exception:
		return -507
	return i


print("\nstarting program one: Inches to yards and feet \n")

i = getNum("Please enter inch value to convert: ")
if(i<0):
	print("invalid inputed! terminating program.")
	sys.exit(0)
print("number in yards: ", ( i * 0.027778))
print("number in feet: ", ( i * 0.0833333))

print("\n------------------------------------------------------------------------- \n " )

print("starting program two: celsius to fahrenheit \n")

i = getNum("Please enter celsius value to convert: ")
if(i == -507):
	print("invalid inputed! terminating program.")
	sys.exit(0)
if(i<-273.15):
	print("Such tempratures not possible! terminating program.")
	sys.exit(0)
print("numer in fahrenheit: ", ( i * (9/5) + 32) )

print("\n------------------------------------------------------------------------- \n" )

print("starting program three: fahrenheit to celsius \n")

i = getNum("Please enter fahrenheit value to convert: ")
if(i == -507):
	print("invalid inputed! terminating program.")
	sys.exit(0)
if(i<-273.15):
	print("Water is too hot")
	sys.exit(0)
print("numer in celsius: ", ( (i-32) * (5/9) ) )

print("\n------------------------------------------------------------------------- \n " )

print("starting program four: yard and feet to inches \n")
yard = getNum("Please enter yard value to convert: ")
feet = getNum("Please enter value in ft to convert: ")
if(yard == -507 or feet == -507):
	print("invalid inputed! terminating program.")
	sys.exit(0)
if(yard <0 or feet<0):
	print("invalid value! terminating program.")
	sys.exit(0)
print("yard in inches: ", (yard * 36))
print("feet in inches: ", (feet * 12))


print("\n------------------------------------------------------------------------- \n" )

print("starting program five: user age \n")

user = getNum("please enter your age: ")
if(user == -507):
	print("invalid inputed! terminating program.")
	sys.exit(0)
if(user<17):
	print("you are a genius")
elif(user >= 17 and user <= 22):
	print("Its college baby lets party!!!!")
elif( user > 22 and user!= 40):
	print("you old as hell you hag")
else:
	print("40 is the new 30")


