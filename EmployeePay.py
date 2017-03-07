'''
******************************************************
@author----->Usama S.

simple program gets hourly wage based on hours wokred\
******************************************************
                                                       '''


def main():
	#get hourly wage and hours worked
	hourlyWage = int(input("Please enter hourly wage: "))
	hoursWorked = int(input("Please enter amount of hours worked: "))
    	amount_to_pay = pay(hourlyWage,hoursWorked)
    	print("your weekly wage is: %d" %amount_to_pay)

def pay(a, b):
	'''
	if hours woked over 40
	get extra hours and multiply by 1.5 and add normal wage
	else return hours by wage
	                          '''
	if b>40:
		extra=b-40
		extra_Pay=extra*a*1.5
		wage=(40*a)+extra_Pay
		return wage
	else:
		wage=a*b
		return wage
#call main
main()
