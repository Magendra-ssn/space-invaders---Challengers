import numpy as np
from PIL import Image
from math import sqrt

img = Image.open("my_picture.jpg")
pixels = np.array(img)

width, height, channels = pixels.shape

actual_width = ...
actual_units = ...

(x1, y1) = ...
(x2, y2) = ...

pixel_distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

actual_distance = (pixel_distance / width) * actual_width

# distance between 2 obstacles = a
# width of obstacle = b
b=float(input("width of obstacle : "))
print("deviate by a distance : ",b+20," mm")
a=float(input("Distance to collsison : "))
print("deviate before : ",2*a," mm")
