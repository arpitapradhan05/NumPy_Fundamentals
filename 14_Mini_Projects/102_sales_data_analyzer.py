import numpy as np

sales = np.array([
    [120, 150, 180, 170, 200],
    [90, 100, 95, 110, 120],
    [200, 220, 210, 230, 240]
])

print("Sales Matrix :\n",sales)

print("Total sales :",np.sum(sales))

print("Total sales of each product :",np.sum(sales,axis = 1))

print("Total sales of each date :",np.sum(sales,axis = 0))

print("Average sales of each product :",np.mean(sales,axis= 1))

print("Highest sales value :",np.max(sales))

print("Lowest sales value :",np.min(sales))

daily_sales = np.sum(sales, axis=0)

print("Total Sales Per Day :", daily_sales)
print("Day Having Maximum Sales :", np.argmax(daily_sales) + 1)

print("Sales values greater than 180 :",sales[sales > 180])

print("Sales number greater than 180 :",np.sum(sales > 180))
