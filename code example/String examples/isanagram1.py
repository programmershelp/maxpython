myString1 = input("Enter the First String  = ")
myString2 = input("Enter the Second String = ")

if(sorted(myString1) == sorted(myString2)):
    print("The Two Strings are Anagrams.")
else:
    print("The Two Strings are not Anagrams.")