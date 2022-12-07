# Enrolments.py
#
# author: Michael Edwards
# date: 31/10/2022
 
distance_from_school = int(input("How many km's do you live from school?"))
age_in_years = int(input("How old are you?"))
has_residency = True
is_fee_foreign = False
print("This program works out eligibility for enrolment....\n")
 
# Test case assertion 1: result should be True
print("The student's eligibility to enrol is ",
      distance_from_school < 4
      and age_in_years < 18
      and age_in_years > 10
      and has_residency
      or age_in_years < 18
      and is_fee_foreign, "\n")
 

