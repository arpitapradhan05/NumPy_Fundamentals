import numpy as np

image = np.array([
    [100, 120, 130, 140],
    [150, 160, 170, 180],
    [190, 200, 210, 220],
    [230, 240, 250, 255]
])

print("Original image :\n",image)

print("Shape :",image.shape)

print("Maximum pixel :",np.max(image))

print("Minimum pixel :",np.min(image))

print("Average brightness :",np.mean(image))

print("Brightness Increased :\n",image + 20)

print("Brightness Decreased :\n",image - 30)

print("Transpose :\n",image.T)

print("Pixels greater than 200:",image[image > 200])

print("Number of Pixels greater than 200:",sum(image > 200))

print("Replaced :\n",np.where(image >= 150, image,0))

