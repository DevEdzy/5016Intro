# DateTest.py
#
# author: Michael Edwards
# date: 29/10/2022
 
from datetime import datetime
from datetime import timedelta
 
date_input = input("Please enter you DOB in the format DD Mmm YYYY: \n")
 
# cast to a datetime object
date_object = datetime.strptime(date_input, '%d %b %Y')
 
# output some confirmation
print ("The year entered is ", date_object.year, "\n")
 
# do a calculation
my_age = datetime.today() - date_object
 
# show the result in different formats
print ("My exact age is ", my_age, "\n")
print ("My exact age just in days is ", my_age.days, "days\n")
print ("My exact age just in years is ", int(my_age.days/365), "years\n")
 
# add 10 days to my current age
print("In 10 days time my age will be ", datetime.today() + timedelta(days=10), ".\n")
 
# add my current age to today's date
print("I will be double my age in ", datetime.today()+ my_age, ".")

# minus 125 days from the date entered
print("The date 125 days prior to when you were born is ", date_object + timedelta(days=-125), ".\n")

# add 2 weeks to the date entered
print("The date 2 weeks after you were born is ", date_object + timedelta(weeks=2), ".\n")

# takes 2 birthdays and returns the age difference
first_date = input("Please enter the first date in the format DD Mmm YYYY: \n")
second_date = input("Please enter the second date in the format DD Mmm YYYY: \n")

# convert variables to datetime object
first_date_object = datetime.strptime(first_date, '%d %b %Y')
second_date_object = datetime.strptime(second_date, '%d %b %Y')

age_difference = (first_date_object - second_date_object)
print("The age difference between the 2 birthdays is ", age_difference, ".\n")

# add number of years to a date entered
date_input = input("Please enter a date in format DD Mmm YYYY: \n")
years = input("Please enter the number of years you would like to increase this date by: \n")

# convert variables to datetime object
date_input_object = datetime.strptime(date_input, "%d %b %Y")
years_object = int(years)
years_days = (years_object * 365)

print("The new date is :", date_input_object + timedelta(days=years_days), ".\n")



