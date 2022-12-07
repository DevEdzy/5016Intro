# BooleanLogicShopping.py
#
# author: Michael Edwards
# date: 31/10/2022

is_registered = False
contains_item = False
guest_login = True
purchasing_giftcard = True

print("User can make a purchase \n")
print(is_registered
      or guest_login
      and contains_item
      or purchasing_giftcard, "\n")
