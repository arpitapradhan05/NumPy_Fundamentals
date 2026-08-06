import numpy as np

arr = np.array([10, 20, 30, 40, 50])
view = arr.view()

view[0] = 100

print("Original :",arr)
print("View :",view)