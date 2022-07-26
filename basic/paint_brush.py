import numpy as np
import cv2 as cv

# mouse callback
def draw_circle(event, x, y, flags, param):
  if event == cv.EVENT_LBUTTONDBLCLK:
    cv.circle(img, (x, y), 100, (255,0,0), -1)

# Create a black image, a window and bind the function to the window
img = np.zeros((512, 512, 3),np.uint8)
cv.namedWindow("Image")
cv.setMouseCallback("Image", draw_circle)

while(True):
  cv.imshow("Image", img)
  if cv.waitKey(20) & 0xFF == 27:
    break
cv.destroyAllWindows()