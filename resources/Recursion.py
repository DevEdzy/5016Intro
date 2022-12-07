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

# Another Example

def collect_folders(start, depth=-1)
    """ negative depths means unlimited recursion """
    folder_ids = []

    # recursive function that collects all the ids in `acc`
    def recurse(current, depth):
        folder_ids.append(current.id)
        if depth != 0:
            for folder in getChildFolders(current.id):
                # recursive call for each subfolder
                recurse(folder, depth-1)

    recurse(start, depth) # starts the recursion
    return folder_ids
