from matplotlib import pyplot as plt

def image(place, img, title, cmap=None):
  plt.subplot(place), plt.imshow(img, cmap=cmap), plt.title(title)

def render():
  plt.show()