import numpy as np

arr = np.array([10, 20, 30, 40, 50])

copy = arr.copy()
copy[0] = 100

print("Original :",arr)
print("Copy :",copy)