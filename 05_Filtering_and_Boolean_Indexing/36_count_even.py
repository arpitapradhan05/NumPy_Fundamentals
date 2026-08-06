import numpy as np

arr = np.array([2, 5, 8, 11, 14, 17, 20])

print(arr % 2 == 0)

count = np.sum(arr % 2 == 0)

print("Even numbers :",count)
