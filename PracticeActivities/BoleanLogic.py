# BooleanLogic.py
#
# author: Michael Edwards
# date: 31/10/2022

is_in_zone = True
is_under_age = True
is_nz_citizen = False
pay_international_fees = True

# Test if a student can enrol at our school
print("The student can enrol at our school \n")
print(is_in_zone
      and is_under_age
      and is_nz_citizen
      or pay_international_fees, "\n")


