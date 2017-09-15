# The goal of this exercise is to produce a binary search algorithm in python.

int_array = [0,11,2,3,4,5,6,34,1]
int_to_find = 0

def searcher(int_to_find,int_array):
    int_array.sort()
    print("Sorting an array of length ", len(int_array))
    x = None
    while x != int_to_find:
        placeholder = len(int_array)//2
        x = int_array[placeholder]

        if x == int_to_find:
            print("Found ",int_to_find, " at ", placeholder)
            return(placeholder)
        elif x > int_to_find:
            print(x, "was too small, chopping off everything after ", placeholder-1)
            int_array = int_array[0:placeholder-1]
        elif x < int_to_find:
            print(x, "was too large, chopping off everything before ", placeholder+1)
            int_array = int_array[placeholder+1:len(int_array)]
