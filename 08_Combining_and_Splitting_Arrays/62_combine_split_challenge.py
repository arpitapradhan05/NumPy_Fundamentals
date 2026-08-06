import numpy as np

arr1 = np.array([10, 20, 30])
arr2 = np.array([40, 50, 60])
arr3 = np.array([70, 80, 90])

combined = np.concatenate((arr1,arr2,arr3))
print(combined)

splited = np.split(combined,3)
print(splited)