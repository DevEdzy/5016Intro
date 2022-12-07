# Using Recursion
def recursive1(i=0):
    ### base case ###
    if i == 9:
        print(f'I have {i} cake(s).')
        return True # return True to stop the loop
    ### base case ###
    print(f'I have {i} cake(s).')
    i+=1 # update the value of i
    return recursive1(i) # return itself with the updated i
recursive1()
