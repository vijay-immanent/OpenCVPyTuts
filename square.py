from cmath import pi
import cv2 as cv
import plt
import json
import numpy as np

from json import JSONEncoder

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

def set_to_list(obj: dict) -> dict:
  """Converts every set in a dictionary to list."""
  newobj = dict()
  for prop in obj:
    if isinstance(obj[prop], set):
      newobj[prop] = list(obj[prop])
    elif isinstance(obj[prop], dict):
      newobj[prop] = set_to_list(obj[prop])
  return newobj



def threshold(img: cv.Mat):
  if img.channels() != 1:
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  print(f"thresholding...")
  _, thresh = cv.threshold(gray, 110, 200, cv.THRESH_BINARY)
  return thresh

def draw_rects(dthresh: cv.Mat, n: int):
  for i in range(0, n):
    contours, _ = cv.findContours(dthresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    print(f"{len(contours)} contours found")
    
    for c in contours:
      # Approximate ploygonal curve of the contour
      approx = cv.approxPolyDP(c, 0.01*cv.arcLength(c, True), True)
      # is a rectangle
      sides = len(approx)

      if sides <= 5:
          cv.drawContours(dthresh, [approx], 0, 200, 10)
      else:
        pass
  
  return dthresh


def dilation(src: cv.Mat, kernel_size: int): 
    element = cv.getStructuringElement(cv.MORPH_RECT, (2 * kernel_size + 1, 2 * kernel_size + 1),
                                       (kernel_size, kernel_size))
    return cv.dilate(src, element)

def identify_rectangles(filename: str, plot=0, imgDir="img", border_width=30) -> tuple[cv.Mat, dict]:
  """Identifies all the rectangular objects in the image file"""
  # Read Image
  print(f"reading: {filename}")
  img = cv.imread(f"{imgDir}/{filename}")
  print(f"converting {filename} to grayscale")
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

  # Threshold
  print(f"thresholding...")
  _, thresh = cv.threshold(gray, 110, 200, cv.THRESH_BINARY)
  
  # Dilate
  dthresh = dilation(thresh, 3)
  dthresh = draw_rects(dthresh, 3)

  plt.subimg(111, dthresh, "RESULT")
  plt.show()
  
  # Identify Contours
  print(f"identifying contours")
  contours, _ = cv.findContours(dthresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
  print(f"{len(contours)} contours found")

  # Find Rectangles
  dimensions = {
    "rectangle": set(),
    "square": set(),
    "polygon": set()
  }
  plots = {
    "square": set(),
    "rectangle": set(),
    "polygon": set()
  }
  for c in contours:
    # Approximate ploygonal curve of the contour
    approx = cv.approxPolyDP(c, 0.01*cv.arcLength(c, True), True)

    # rectangle
    if len(approx) == 4:
      x, y, w, h = cv.boundingRect(approx)
      cv.drawContours(dthresh, [approx], 0, 200, 5)
      if w == h:
        # perfect square
        plots["square"].add((x, y, w, h))
        dimensions["square"].add((w, h))
        cv.drawContours(img, [approx], 0, (255, 255, 255), border_width)
      elif abs(w - h) <= 2:
        # approximate square
        plots["square"].add((x, y, w, h))
        dimensions["square"].add((w, h))
        cv.drawContours(img, [approx], 0, (255, 255, 255), border_width)
      else:
        # not a square
        plots["rectangle"].add((x, y, w, h))
        dimensions["rectangle"].add((w, h))
        # print("RECT", x, y, w, h)
        cv.drawContours(img, [approx], 0, (255, 0, 0), border_width)

        # draw the rectangle
        # cv.drawContours(img, [approx], 0, (255, 0, 0), 4)
    else:
      x, y, w, h = cv.boundingRect(approx)
      # print("POLYGON", x, y, w, h)
      plots["polygon"].add((x, y, w, h))
      dimensions["polygon"].add((w, h))
      cv.drawContours(img, [approx], 0, (255, 0, 0), border_width)

  # print(len(dimensions), ':\n\t', dimensions)
  print(f'{len(plots["rectangle"])} rectangles found')
  print(f'{len(plots["square"])} squares found')
  print(f'{len(plots["polygon"])} polygons found')

  if plot != 2:
    def showImagePlot():
      if plot == 2:
        plt.subimg(131, gray, "GRAY")
        plt.subimg(132, thresh, "THRESHOLD")
        plt.subimg(133, img, "Result")
      elif plot == 1:
        plt.subimg(111, img, "RESULT")
      plt.show()
    showImagePlot()

  return (img, {"dimensions": dimensions, "plots": plots})


def save_as_json(data, filename: str):
  if isinstance(data, dict):
    data = set_to_list(data)
  data = json.dumps(data, cls=NumpyArrayEncoder)
  with open(filename, "w") as outfile:
    outfile.write(data)


def contours(filename: str, imgDir="img") -> tuple[cv.Mat, any]:
  """Identifies all the rectangular objects in the image file"""
  # Read Image
  print(f"reading: {filename}")
  img = cv.imread(f"{imgDir}/{filename}")
  print(f"converting {filename} to grayscale")
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

  # Threshold
  print(f"thresholding...")
  _, thresh = cv.threshold(gray, 110, 200, cv.THRESH_BINARY)

  # Dilate
  dthresh = dilation(thresh, 3)
  dthresh = draw_rects(dthresh, 3)

  # plt.subimg(111, dthresh, "RESULT")
  # plt.show()

  # Identify Contours
  print(f"identifying contours")
  contours, _ = cv.findContours(dthresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
  print(f"{len(contours)} contours found")

  return dthresh, contours

if __name__ == "__main__":
  filename = "boxmap-land-trace.png"
  thresh, img_contours = contours(filename)

  # jsonify
  jsonfile = f"json/{filename.split('.')[0]}-contours.json"
  save_as_json(img_contours, jsonfile)

  cv.imwrite("contours/" + "contours-" +filename, thresh)

