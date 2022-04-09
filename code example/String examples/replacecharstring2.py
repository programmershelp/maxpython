# Replace a Character in a String Using a For Loop
# User Input
string1 = input("Please Enter your String : ")
character1 = input("Please Enter your Own Character : ")
newcharacter1 = input("Please Enter the New Character : ")

string2 = ''
for i in range(len(string1)):
    if(string1[i] == character1):
        string2 = string2 + newcharacter1
    else:
        string2 = string2 + string1[i]

print("Original String : ", string1)
print("\nModified String : ", string2)