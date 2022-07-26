import cv2 as cv
import numpy as np
# from matplotlib import pyplot as plt


def bgr_to_gray(img):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)


def bgr_to_hsv(b, g, r):
  color = np.uint8([[[b, g, r]]])
  hsv_color = cv.cvtColor(color, cv.COLOR_BGR2HSV)
  return hsv_color


def getAllColorConversionFlags():
    return [i for i in dir(cv) if i.startswith("COLOR_")]


def track_object():
    cap = cv.VideoCapture(0)
    while (True):
        # take each frame
        _, frame = cap.read()

        # convert bgr to hsv
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # define range of color in HSV
        lower = np.array([0, 10, 60], dtype="uint8")
        upper = np.array([20, 150, 255], dtype="uint8")

        # threshold the hsv image to get only target colors
        mask = cv.inRange(hsv, lower, upper)

        # bitwise-AND mask and original image
        res = cv.bitwise_and(frame, frame, mask=mask)

        cv.imshow('frame', frame)
        cv.imshow("mask", mask)
        cv.imshow("res", res)
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            break


cv.destroyAllWindows()

if __name__ == "__main__":
    track_object()
