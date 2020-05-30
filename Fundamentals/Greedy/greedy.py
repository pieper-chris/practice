import random

# Basic search algorithms and their complexities

# Bubble Sort
def bubble_sort(lst):
    lst_len = len(lst)
    if (lst_len < 2): return lst
    for i in range(lst_len):
        for j in range(lst_len - 1 - i):
            if (lst[j] > lst[j+1]):
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst


# Insertion Sort
def insertion_sort(lst):
    lst_len = len(lst)
    if (lst_len < 2): return lst
    for right in range(1,lst_len):
        left = 0
        while(lst[right] > lst[left]): left +=1
        temp = lst[right]
        # linear search for placement
        for k in range((right-left)):
            lst[right-k] = lst[right-k-1]
        lst[left] = temp
    return lst



'''-------------Script for bubble_sort()----------------------'''
# 1-elt test
print(bubble_sort([]))
print(bubble_sort([9]))

# Small list test
print(bubble_sort([6,5,7,5,3,4,1]))

# Larger tests...
result = bubble_sort(random.sample(range(0, 500), 300))
print(result[:10],"...",result[-10:])
        

'''-------------Script for insertion_sort()----------------------'''
# 1-elt test
print(insertion_sort([]))
print(insertion_sort([9]))

# Small list test
print(insertion_sort([6,5,7,5,3,4,1]))

# Larger tests...
result = insertion_sort(random.sample(range(0, 500), 300))
print(result[:10],"...",result[-10:])
