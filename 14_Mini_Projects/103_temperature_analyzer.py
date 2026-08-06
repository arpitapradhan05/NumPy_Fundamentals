import numpy as np

temperature = np.array([32, 35, 30, 28, 36, 40, 38, 31, 29, 34])

print("Temperatures :",temperature)

print("Average Temperature :",np.mean(temperature))

print("Highest Temperature :",np.max(temperature))

print("Lowest Temperature :",np.min(temperature))

print("Difference :",np.max(temperature) - np.min(temperature))

print("Highest Temperature Day :",np.argmax(temperature)+1)

print("Lowest Temperature Day :",np.argmin(temperature)+1)

print("Temperatures greater than average :",temperature[temperature > np.mean(temperature)])

print("Days with Temperatures greater than average :",np.sum(temperature > np.mean(temperature)))

print("Temperature greater than 35 :",temperature[temperature > 35])

print("Count of Hot days :",np.sum(temperature > 35))