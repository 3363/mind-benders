# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(list, e):
    answer = -1
    i = 0
    
    while i < len(list):
        if list[i] == e:
            return i
        i += 1
    return answer




print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1


#++++++

# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element_idx(list, e):
    i = 0
    while i < len(list):
        if list[i] == e:
            return list.index(e)
        i += 1
    
    return -1




print find_element_idx([1,2,3],3)
#>>> 2

print find_element_idx(['alpha','beta'],'gamma')
#>>> -1
