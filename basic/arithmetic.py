import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img1 = cv.imread("img/eagle_logo.jpg")
img2 = cv.imread("img/cat_logo.jpg")
plt.subplot(231), plt.imshow(img1, "gray"), plt.title("img1")
plt.subplot(234), plt.imshow(img2, "gray"), plt.title("img2")

# Numpy Addition
np_add = img1 + img2
plt.subplot(232), plt.imshow(np_add, "gray"), plt.title("NP ADDITION")
# CV Addition
cv_add = cv.add(img1, img2)
plt.subplot(235), plt.imshow(cv_add, "gray"), plt.title("CV ADDITION")

# image blending: alpha
blended = cv.addWeighted(img1, 0.5, img2, 0.5, 0)
plt.subplot(233), plt.imshow(blended, "gray"), plt.title("CV BLENDED")




plt.show()