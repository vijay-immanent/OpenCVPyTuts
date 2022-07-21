import cv2 as cv
from matplotlib import pyplot as plt

print(cv.setUseOptimized(True))
def time(e1, e2):
  t = (e2 - e1) / cv.getTickFrequency()
  print("time:", t)
  return t

img = cv.imread("img/dr_azumi.png")

e1 = cv.getTickCount()
for i in range(5, 92, 2):
  img = cv.medianBlur(img, i)
e2 = cv.getTickCount()
time(e1, e2)

plt.subplot(111), plt.imshow(img, "gray"), plt.title("Median Blur")
plt.show()