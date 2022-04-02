# Numpy Array Arithemetic Operations
import numpy as np

nparr1 = np.array([10, 20, 30, 40, 50])
nparr2 = np.array([6, 13, 5, 21, 9])


addarr = nparr1 + nparr2
subarr = nparr1 - nparr2
mularr = nparr1 * nparr2
modarr = nparr1 % nparr2
divarr = nparr1 / nparr2

print("After arithmetic operations")
print("Array Addition = ", addarr)
print("Array Subtraction = ", subarr)
print("Array Multiplication =  ", mularr)
print("Array Modulus = ", modarr)
print("Array division = ", divarr)