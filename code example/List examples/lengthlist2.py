from operator import length_hint
 
# Initializing list
myList = ['This', 'is', 'a', 'string', 'list']
 
# Printing test_list
print ("The list is : " + str(myList))
 
# Finding length of list using len()
listlength = len(myList)
 
# Finding length of list using length_hint()
listlengthhint = length_hint(myList)
 
# Printing length of list
print ("Length of list using len() is : " + str(listlength))
print ("Length of list using length_hint() is : " + str(listlengthhint))