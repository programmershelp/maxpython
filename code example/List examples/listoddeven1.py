# Program to Count Even and Odd Numbers in a List
mylist = []
even_numbers = 0
odd_numbers = 0

# Get user input
Number = int(input("Please enter the Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of Element %d : " %i))
    mylist.append(value)

# loop through and count even and odd numbers
for j in range(Number):
    if(mylist[j] % 2 == 0):
        even_numbers = even_numbers + 1
    else:
        odd_numbers = odd_numbers + 1
        
#Print the counts
print("\nTotal Number of Even Numbers in this List =  ", even_numbers)
print("Total Number of Odd Numbers in this List = ", odd_numbers)