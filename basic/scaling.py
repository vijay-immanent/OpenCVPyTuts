import cv2 as cv
import numpy as np
import show

if __name__ == "__main__":
  img = cv.imread("img/face.png")
  show.image(121, img, "Original")

  res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)

  show.render()

def rescale(frame, scale=0.75):
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)
  dimensions = (width, height)

  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

