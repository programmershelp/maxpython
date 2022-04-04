myString = input("Please enter the Your Own String = ")
dictchars = {}

for num in myString:
    keys = dictchars.keys()
    if num in keys:
        dictchars[num] += 1
    else:
        dictchars[num] = 1

print(dictchars)