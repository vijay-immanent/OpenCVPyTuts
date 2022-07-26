import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 3px
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 3)

# Rectangle: top-left and bottom-right corner
cv.rectangle(img, (384, 1), (510, 128), (0, 255, 0), 3)

# Circle: center and radius
cv.circle(img, (447, 64), 63, (0, 0, 255), -1)

# Ellipse
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# Polygon
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0, 255, 255))

# Text
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)

# show image
cv.imshow("Shapes", img)
cv.waitKey(0)