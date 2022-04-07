NumberList = []
Number = int(input("Please enter the Total Number of Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumberList.append(value)

print("The Smallest Element in the List is : ", min(NumberList))
print("The Largest Element in the List is : ", max(NumberList))