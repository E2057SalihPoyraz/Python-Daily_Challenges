# QUESTION:
# This is an interview question asked by Facebook.
# Given an array of integers, write a function to determine whether the array could become
# non-decreasing by modifying at most 1 element. For example, given the array [10, 5, 7], you should
# return true, since we can modify the 10 into a 1 to make the array non-decreasing. Given the
# array [10, 5, 1], you should return false, since we can't modify any one element to get a
# non-decreasing array.

# Çözüm-1
def check1(lst):
    count = 0
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            if count > 1:
                return False
            if i>1 and i<len(lst)-2 and lst[i-1] > lst[i+1] and lst[i] > lst[i+2]:
                return False    
            count += 1       
    return True

# Çözüm-2
def check2(lst):
    count = 0
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            if i>1 and i<len(lst)-2 and lst[i-1] > lst[i+1] and lst[i] > lst[i+2]:
                return False    
            count += 1
    return bool(count<2) and True or False