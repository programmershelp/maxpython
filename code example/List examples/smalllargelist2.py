NumberList = []
Number = int(input("Please enter the Total Number of Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumberList.append(value)

NumberList.sort()

print("The Smallest Element in the List is : ", NumberList[0])
print("The Largest Element in the List is : ", NumberList[Number - 1])