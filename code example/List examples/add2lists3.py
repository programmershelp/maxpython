# Add two Lists using map() with add operator
from operator import add

# initializing lists
list1 = [10, 20, 30, 40, 50]
list2 = [5, 10, 15, 20, 25]
total = []

# print original lists
print ("list 1 : " + str(list1))
print ("list 2 : " + str(list2))

# using map() + add() to add the lists
total = list(map(add, list1, list2))

# printing list
print ("\nThe total Sum of Two Lists =  " + str(total))