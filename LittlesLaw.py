arrivalRate = 0
timeSpent = 0
avgCustomers = 0

# setup choice, looking for average number, arrival rate, or average time in system

print("Are you trying to find:")
print("1: The long term average number of customers in a stable system")
print("2: The long term average effective arrival rate")
print("or")
print("3: The average time a customer spends in the system?")

selection = int(raw_input())

if selection == 1:
	print("What is the average arrival rate per hour?")
	arrivalRate = int(raw_input())
	print("What is the average time, in minutes, that a customer stays in the system?")
	timeSpent = int(raw_input())
	print("Your average number of customers within the system is " + str(int(arrivalRate * int(timeSpent*0.0166))))
elif selection == 2:
	print("What is the average time, in minutes, that a customer stays in the system?")
	timeSpent = int(raw_input())
	print("What is the average number of customers in the system?")
	avgCustomers = int(raw_input())
	print("The average arrival rate is " + str(int(avgCustomers/(timeSpent*0.0166))) + " customers per hour.")
elif selection == 3:
	print("What is the average number of customers in the system?")
	avgCustomers = int(raw_input())
	print("What is the average arrival rate per hour?")
	arrivalRate = int(raw_input())
	print("The average number of minutes a customer spends in the system is " + str(avgCustomers/(arrivalRate/60)))
else:
	print("You selected " + str(selection) + ", please select 1, 2 or 3.")
