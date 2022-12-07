Hi team, 

Does anyone know why my code below always returns "correct" regardless of the answer provided:

question_one = input("What city in New Zealand has the steepest street in the world? \n"
                     "a. Auckland \n"
                     "b. Dunedin \n"
                     "c. Christchurch \n")

if question_one == "b" or "B":
    print("correct")
elif question_one != "b" or "B":
    print("incorrect")

# Answered provided by course co-ordinator.

question_one = input("What city in New Zealand has the steepest street in the world? \n"
                     "a. Auckland \n"
                     "b. Dunedin \n"
                     "c. Christchurch \n")

if question_one == ("b" or "B"):
    print("correct")
elif question_one != ("b" or "B"):
    print("incorrect")
