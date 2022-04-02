import numpy as np

originalarray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

copyarray1 = originalarray
copyarray2 = originalarray[3:7]
copyarray3 = originalarray[4:]
copyarray4 = originalarray[::-1]

print("Original Array = ", originalarray)
print("Copied Array   = ", copyarray1)
print("Copy Array Items 4 to 7   = ", copyarray2)
print("Copy Array Items 5 to End   = ", copyarray3)
print("Reverse Array   = ", copyarray4)