import numpy as np
import matplotlib
from PIL import Image
from matplotlib import pyplot as plt

pic = Image.open('00-puppy.jpg')

print(type(pic))
pic_arr = np.asarray(pic)
print(type(pic_arr))

print(pic_arr.shape)
plt.imshow(pic_arr)
plt.show()

pic_red = pic_arr.copy()
plt.imshow(pic_arr)
plt.show()

# R : 0, G : 1, B : 2
# only red channel
plt.imshow(pic_red[:, :, 0])
plt.show()

plt.imshow(pic_red[:, :, 0], cmap='gray')
plt.show()

# remove green
pic_red[:, :, 1] = 0
plt.imshow(pic_red)
plt.show()

# remove blue
# only red (removed blue and green)
pic_red[:, :, 2] = 0
