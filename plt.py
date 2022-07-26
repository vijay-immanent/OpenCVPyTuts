from matplotlib import pyplot as plt
import cv2 as cv

def subimg(place: int, img: cv.Mat, title="Image", cmap="gray"):
  plt.subplot(place), plt.imshow(img, cmap=cmap), plt.title(title)

def show():
  plt.show()