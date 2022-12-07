# ParkingMeter.py
#
# author: Michael Edwards
# date: 31/10/2022
 
print ("Kia Ora, this is a parking meter \n")
park_time = int(input("Please enter number of hours you would like to park for \n"))
print ("park_time time is ", park_time, " hours.")
 
rate = 4
cost = 0
if park_time > 3:
    cost = rate *3
    # drop the rate by $2
    rate -= 2
    # get the remainder of the parking time
    park_time -= 3
    # add to the current cost
    cost += rate * park_time
    print("The cost of the parking is $", cost)
else:
    cost = rate * park_time
    print ("The cost of the parking is $", cost)
