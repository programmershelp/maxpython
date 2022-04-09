# Python Program to Add Two Lists Using List Comprehension method

list1 = [10, 20, 30, 40, 50]
list2 = [5, 10, 15, 20, 25]
total = []

print ("List 1 : " + str(list1))
print ("List 2 : " + str(list2))

# using list comprehension to add the two lists
total = [list1[i] + list2[i] for i in range(len(list1))]

# printing resultant list
print ("Resultant list is : " + str(total))