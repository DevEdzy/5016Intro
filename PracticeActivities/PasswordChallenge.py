# PasswordChallenge.py

# author: Michael Edwards
# date: 4/11/2022


user_input = input("Please enter your password")
password = "chocolate"
attempts = 0
correct = False

while attempts < 2 and correct == False:
    if user_input == password:
        print("Correct")
        correct = True
    elif password == "Exit":
        print("Terminated")
        correct = True
    else:
        print("Incorrect, please try again")
        user_input = input("Please enter your password")
        attempts += 1
