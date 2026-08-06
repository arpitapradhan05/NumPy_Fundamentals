import numpy as np

np.random.seed(42)

marks = np.random.randint(0, 101, 20)

print("Marks :",marks)

print("Total Marks :",np.sum(marks))

print("Average Marks :",np.mean(marks))

print("Highest Marks :",np.max(marks))

print("Lowest Marks :",np.min(marks))

print("Index of Topper :",np.argmax(marks))

print("Index of Lowest marks :",np.argmin(marks))

print("Marks more than 75 :",marks[marks > 75])

print("Number of students scoring more than 75 :",sum(marks > 75))

print("Failed stdents :",marks[marks < 40])

print("Number of student failed :",sum(marks < 40))

asc_marks = np.sort(marks)

print("Ascending Order :", asc_marks)

desc_marks = asc_marks[::-1]

print("Descending Order :", desc_marks)

print("Top 5 Highest Marks :", desc_marks[:5])