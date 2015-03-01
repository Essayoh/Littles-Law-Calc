arrivalRate = 0
timeSpent = 0

print("What is the average arrival rate per hour?")
arrivalRate = int(raw_input())

print("What is the average time, in minutes, that a customer stays in the system?")
timeSpent = int(raw_input())

print("Your average number of customers within the system is " + str(int(arrivalRate * (timeSpent*0.0166))))