import numpy as np
import cv2 as cv

# accessing and modifying pixel values
img = cv.imread("img/face.png")

px = img[100, 100]  # returns BGR values at the index
print("BGR:", px)
g = img[100, 100, 1]  # returns Green intensity of the
print("Green:", g)

# modify pixel value
img[100, 100, 1] = 255
print("BGR:", px)

# optimised numpy methods
img.itemset((100, 100, 2), 255)
opx = img.item(100, 100, 2)
print("Red:", opx, "BGR:", px)

# Image Properties
# greyscale images don't return channels in shape
print("(rows, columns, channels)", img.shape)
print("total number of pixels:", img.size)
print("image datatype:", img.dtype)


# Image ROI
region = img[280:340, 330:390]
img[273:333, 100:160] = region
# cv.imshow("Img", img)
# cv.waitKey(0)

# Splitting Channels
b,g,r = cv.split(img) # split all channels
b = img[:,:,0] # extract blue from all pixels
img[:,:,2] = 0 # set red in all pixels to zero

