import numpy as np

marks = np.array([45, 78, 92, 56, 88, 34, 95, 67])

print("80 Above :",np.where(marks > 80))

print("Highest marks :",np.max(marks))
print("Highest marks index :",np.argmax(marks))

print("Lowest marks :",np.min(marks))
print("Lowest marks index :",np.argmin(marks))
 
