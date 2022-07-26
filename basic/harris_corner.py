import numpy as np
import cv2 as cv
import plt


def harris_corner(img: cv.Mat):
  gray = np.float32(img)
  plt.subimg(231, gray, "GRAY", "gray")
  dst = cv.cornerHarris(gray, 2, 3, 0.04)
  # Dilate the result for marking the corners
  dst = cv.dilate(dst, None)
  plt.subimg(232, dst, "Corner Harris", "gray")

  gray[dst>0.01*dst.max()]= 0
  plt.subimg(233, gray, "RESULT", "gray")
  
  return dst

def corner_subpixel_accuracy(img: cv.Mat, gray: cv.Mat, dst: cv.Mat):
  ret, dst = cv.threshold(dst, 0.01*dst.max(), 255, 0)
  dst = np.uint8(dst)

  # find centroids
  ret, labels, stats, centroids = cv.connectedComponentsWithStats(dst)

  # define criteria to stop and refine the corners
  criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
  corners =cv.cornerSubPix(gray, np.float32(centroids), (5,5), (-1, -1), criteria)

  # draw
  res = np.hstack((centroids, corners))
  res = np.int0(res)
  img[res[:,1], res[:,0]] = [0, 0,255]
  img[res[:,3], res[:,2]] = [0, 255, 0]

  img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

  plt.subimg(236, img, "SubPixel") 


if __name__ == "__main__":
  filename ="img/color_grid.png"
  img = cv.imread(filename)
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  
  dst = harris_corner(gray.copy())
  corner_subpixel_accuracy(img.copy(), gray.copy(), dst)
  
  plt.show()