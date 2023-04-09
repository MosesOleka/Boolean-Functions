# A Python function that takes 10 lists and returns True 
# if they have at least one common member

list1 = ['a', 'b', 'c']
list2 = ['a', 'z', 'c']
list3 = ['a', 'x', 'c']
    
common_elements = list(set(list1).intersection(list2, list3))


def cohort_5():
    if common_elements:
        print("True", "the common elements are", common_elements)
    else:
        print("False", "there are no common")




cohort_5()




# Assignment 2
