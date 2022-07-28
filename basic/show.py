from matplotlib import pyplot as plt
import cv2 as cv

def image(place: int, img: cv.Mat, title="Image", cmap="gray"):
  plt.subplot(place), plt.imshow(img, cmap=cmap), plt.title(title)

def render():
  plt.show()


def main():
  filename = "contours/world_map.jpg"
  img = cv.imread(filename)
  image(111, img, filename)
  render()

if __name__ == "__main__":
  main()