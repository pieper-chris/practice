# Basic search algorithms and their complexities

# Linear search (ints)
# pass in the element (int) to be found and an int list to search in (can be unsorted)
# returns index of 1st-found element to match 'elt', returns -1 if DNE
def linear_search(elt, lst):
    idx = 0
    lst_size = len(lst)
    while((idx<lst_size) and (elt != lst[idx])): idx += 1
    if (idx < lst_size): return idx
    else: return -1
    
# binary search (ints)
# pass in the element (int) to be found and an int list to search in (must be unsorted)
# returns index of 1st-found element to match 'elt', returns -1 if DNE
def binary_search(elt, lst):
    lst_size = len(lst)
    l = 0 # left endpoint
    r = (lst_size - 1) # right endpoint
    while(l < r):
        midpoint = (l+r)//2 # need to specify floor division // in python3
        if(elt > lst[midpoint]): l = midpoint + 1
        else: r = midpoint
    if (elt == lst[l]): return l
    else: return -1
    
    
    
    

'''Example scripts for linear_search() below - uncomment to run'''

# should return -1
# print(linear_search(5, [3,6,6,4,3,2,4,6]))

# should return 2 ("third index", as 1st index is 0)
# print(linear_search(5, [3,6,5,4,3,2,4,6]))

'''Example scripts for binary_search() below - uncomment to run
   (Uses python3 sorted() function for passed parameters)'''
   
# Note: python uses timesort (https://en.wikipedia.org/wiki/Timsort)

# should return -1
# print(binary_search(5, sorted([3,6,6,4,3,2,4,6])))

# should return 5 ("6th index", as 1st index is 0)
# print(binary_search(5, sorted([3,6,5,4,3,2,4,6])))

