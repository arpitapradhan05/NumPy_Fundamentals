import numpy as np

A = np.array([
    [2, 3],
    [1, 4]
])

B = np.array([
    [5, 1],
    [2, 3]
])

print("Addition :\n")
print(A + B)

print("Element by element multiplication :\n")
print(A * B)

print("Matrix multiplication :\n")
print(A @ B)

print("Transpose of A matrix :\n")
print(A.T)

print("Determinant of A matrix :\n")
print(np.linalg.det(A))

print("Inverse of A matrix :\n")
print(np.linalg.inv(A))