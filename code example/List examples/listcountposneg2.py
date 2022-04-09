# Count the Positive and Negative Numbers in a List Using a While Loop

mylist = []
positive_number = 0
negative_number = 0
j = 0

# Input From the User
Number = int(input("Enter the Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Enter the Value of Element %d : " %i))
    mylist.append(value)

# Print the List Entered by the User
print("Users list is: ",mylist)

#loop through incrementing counts
while(j < Number):
    if(mylist[j] >= 0):
        positive_number = positive_number + 1
    else:
        negative_number = negative_number + 1
    j = j + 1

# Print the totals
print("\nTotal Number of Positive Numbers in the List =  ", positive_number)
print("\nTotal Number of Negative Numbers in the List = ", negative_number)