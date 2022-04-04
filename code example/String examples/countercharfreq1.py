from collections import Counter

myString = input("Please enter the Your Own String = ")

chars = Counter(myString)

print("Total Character Frequency in this String = ")
print(chars)