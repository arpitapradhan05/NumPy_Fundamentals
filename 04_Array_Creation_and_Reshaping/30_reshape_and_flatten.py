import numpy as np

arr = np.arange(1, 13)

reshaped_arr = arr.reshape(3,4)

print("Resahped :\n",reshaped_arr)

print("Flattened :",reshaped_arr.flatten())