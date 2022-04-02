import numpy as np

originalarray = np.array([10, 20, 30, 40, 50])
copyarray = np.empty(5)

for i in range(len(originalarray)):
    copyarray[i] = originalarray[i]

print("Original Array = ", originalarray)
print("Copy Of Array   = ", copyarray)