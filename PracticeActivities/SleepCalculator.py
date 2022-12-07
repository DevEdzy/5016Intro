# SleepCalculator.py
#
# author: Michael Edwards
# date: 29/10/2022

print("Welcome")

birth_year = int(input("what year were you born: "))
average_sleep = 7
current_year = 2022
days = 365
total_hours_slept = (((current_year - birth_year) * days) * average_sleep)

print(total_hours_slept)

# Calculates total hours slept by a person in their lifetime
