# Quiz.py
#
# author: Michael Edwards
# date: 31/10/2022

question_one = input("What city in New Zealand has the steepest street in the world? \n"
                     "a. Auckland \n"
                     "b. Dunedin \n"
                     "c. Christchurch \n")

score = 0

if question_one.lower() == "b":
    print("correct")
    score += 1
    print("Your score is now ", score, "\n")
else:
    print("incorrect")
    print ("Your score is still ", score, "\n")


# if statement practice

