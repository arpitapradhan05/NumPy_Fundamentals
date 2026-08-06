import numpy as np

arr = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50])

new_arr = arr[(arr > 20) & (arr < 45)]

print(new_arr)

