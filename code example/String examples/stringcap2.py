# How To Capitalize First Letter of Each Word of a String in Python
# using the capswords() Method
import string

string1='This is my sample text message'
print(string.capwords(string1))

string2='THIS IS MY SAMPLE TEXT MESSAGE'
print(string.capwords(string2))

string3='This IS my sAMple TEXt mEsSage'
print(string.capwords(string3))