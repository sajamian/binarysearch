def recursive_search(int_to_find, int_array, lbound = 0, rbound = None):
    if not rbound:
        rbound = len(int_array)-1
    if lbound == rbound == int_to_find:
        return(lbound)
    else:
        midpoint = (rbound - lbound)//2
        if int_array[lbound + midpoint] == int_to_find:
            return(lbound + midpoint)
        elif int_array[lbound + midpoint] < int_to_find:
            lbound += max(midpoint, 1) # We should at least iterate by 1, since // skews left.
            return recursive_search(int_to_find, int_array, lbound, rbound)
        elif int_array[rbound - midpoint] > int_to_find:
            rbound -= midpoint
            return recursive_search(int_to_find, int_array, lbound, rbound)
        
