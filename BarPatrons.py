# BarPatrons.py
#
# author: Michael Edwards
# date: 31/10/2022

yob = int(input("what year were you born?"))
age = 2022 - yob
name = input("What is your name?")

print("You can enter the bar")

print(age > 21
      and name != "Suzanne May"
      and name != "Wiremu Rangi", "\n")
