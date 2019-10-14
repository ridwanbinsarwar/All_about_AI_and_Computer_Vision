import numpy as np;
from matplotlib import pyplot as plt

import cv2
img = cv2.imread('00-puppy.jpg')

plt.imshow(img)
plt.show()

# MATPLOTLIB  --> RGB RED GREEN BLUE
# OPENCV -- > BLUE GREEN RED

fixedImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(fixedImage)
plt.show()

img_gray = cv2.imread('00-puppy.jpg', cv2.IMREAD_GRAYSCALE)
fixedImage = cv2.cvtColor(img_gray, cv2.COLOR_BGR2RGB)
plt.imshow(fixedImage)
plt.show()


