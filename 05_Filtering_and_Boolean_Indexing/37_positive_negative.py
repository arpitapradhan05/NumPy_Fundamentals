import numpy as np

arr = np.array([-10, 20, -5, 30, -15, 40, 50])

positive = arr[arr >= 0]

negative = arr[arr < 0]

print("Positive :",positive)

print("Negative :",negative)

