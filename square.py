import cv2 as cv
import plt
import json

def set_to_list(obj: dict):
  newobj = dict()
  for prop in obj:
    if isinstance(obj[prop], set):
      newobj[prop] = list(obj[prop])
    elif isinstance(obj[prop], dict):
      newobj[prop] = set_to_list(obj[prop])
  return newobj



def main(filename: str):
  img = cv.imread(f"img/{filename}")
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  _, thresh = cv.threshold(gray, 110, 200, cv.THRESH_BINARY)
  contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

  map = {
    "dimensions": {
      "rectangle": set(),
      "square": set()
    },
    "plots": {
      "square": set(),
      "rectangle": set()
    }
  }
  print("contours:", len(contours))
  for c in contours:
    approx = cv.approxPolyDP(c, 0.01*cv.arcLength(c, True), True)
    x, y, w, h = cv.boundingRect(approx)
    if len(approx) == 4:
      cv.drawContours(img, [approx], 0, (255, 0, 0), 2)
      if w == h:
        map["plots"]["square"].add((x, y, w, h))
        map["dimensions"]["square"].add((w, h))
        print("SQUARE", x, y, w, h)
      elif abs(w - h) <= 2:
        map["plots"]["square"].add((x, y, w, h))
        map["dimensions"]["square"].add((w, h))
      else:
        map["plots"]["rectangle"].add((x, y, w, h))
        print("RECT", x, y, w, h)
        map["dimensions"]["rectangle"].add((w, h))


  # print(len(dimensions), ':\n\t', dimensions)
  print(len(map["plots"]["rectangle"]))
  print(len(map["plots"]["square"]))


  def show():
    plt.subimg(131, gray, "GRAY")
    plt.subimg(132, thresh, "THRESHOLD")
    plt.subimg(133, img, "Result")
    plt.show()
  show()
  cv.imwrite("contours/" + filename, img)
  data = set_to_list(map)
  serialized_data = json.dumps(data, indent=2 )
  with open(f"json/{filename.split('.')[0]}.json", "w") as outfile:
    outfile.write(serialized_data)




if __name__ == "__main__":
  filename = "world_map.jpg"
  main(filename)