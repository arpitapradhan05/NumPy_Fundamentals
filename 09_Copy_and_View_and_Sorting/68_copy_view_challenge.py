import numpy as np

arr = np.array([10, 20, 30, 40])

copy_arr = arr.copy()
view_arr = arr.view()

copy_arr[0] = 100
view_arr[1] = 200

print("Original :",arr)
print("Copy :",copy_arr)
print("View :",view_arr)
