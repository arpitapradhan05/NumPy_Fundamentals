import numpy as np

marks = np.array([78, 56, 92, 45, 88, 67, 95, 73])

print("All Marks :",marks)

print("Total marks :",np.sum(marks))
print("Average marks :",np.mean(marks))

print("Highest marks :",np.max(marks))
print("Lowest marks :",np.min(marks))
print("Highest marks Index :",np.argmax(marks))
print("Lowest marks Index:",np.argmin(marks))

print("Above 80 :",np.where(marks > 80, marks , 0)) #method 1
print("Above 80 :",marks[marks > 80]) #method 2

print("Passed Students :", marks[marks >= 40])
print("Number of Passed Students :", np.sum(marks >= 40))

print("Above average number :",marks[marks >= np.mean(marks) ])