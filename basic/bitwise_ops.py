import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

art = cv.imread("img/bamboo_art.jpg")
eagle = cv.imread("img/eagle_logo.jpg")

rows, cols, channels = eagle.shape
roi = art[0:rows, 0:cols]
# plt.subplot(111), plt.imshow(roi, "gray"), plt.title("ROI")

eagleGray = cv.cvtColor(eagle, cv.COLOR_BGR2GRAY)
plt.subplot(231), plt.imshow(eagleGray, "gray"), plt.title("EAGLE GRAY")

ret, mask = cv.threshold(eagleGray, 10, 255, cv.THRESH_BINARY)
plt.subplot(232), plt.imshow(mask, "gray"), plt.title("MASK")
mask_inv = cv.bitwise_not(mask)
plt.subplot(233), plt.imshow(mask_inv, "gray"), plt.title("MASK INV")

art_bg = cv.bitwise_and(roi, roi, mask=mask)
plt.subplot(234), plt.imshow(art_bg, "gray"), plt.title("ART BG")
eagle_fg = cv.bitwise_and(eagle, eagle, mask=mask_inv)
plt.subplot(235), plt.imshow(eagle_fg, "gray"), plt.title("EAGLE FG")

dst = cv.add(art_bg, eagle_fg)
plt.subplot(236), plt.imshow(dst, "gray"), plt.title("DST")
art[0:rows, 0:cols] = dst

# plt.subplot(237), plt.imshow(art, "gray"), plt.title("RESULT")
plt.show()
