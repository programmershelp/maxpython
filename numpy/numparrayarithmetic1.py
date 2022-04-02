# Numpy Array Arithemetic Operations
import numpy as np

nparr1 = np.array([10, 20, 30, 40, 50])
nparr2 = np.array([6, 13, 5, 21, 9])

addarr = np.add(nparr1, nparr2)
subarr = np.subtract(nparr1, nparr2)
mularr = np.multiply(nparr1, nparr2)
modarr = np.mod(nparr1, nparr2)
remarr = np.remainder(nparr1, nparr2)
divarr = np.divide(nparr1, nparr2)

print("After arithmetic operations")
print("Array Addition = ", addarr)
print("Array Subtraction = ", subarr)
print("Array Multiplication =  ", mularr)
print("Array Modulus = ", modarr)
print("Array Remainder = ", remarr)
print("Array division = ", divarr)