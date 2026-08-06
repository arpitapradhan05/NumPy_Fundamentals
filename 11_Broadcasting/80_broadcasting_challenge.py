import numpy as np

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 78]
])

bonus = np.array([5, 5, 5])

print("Original :\n",marks)
print("Bonus :\n",bonus)

print("Updated marks :\n",marks + bonus)