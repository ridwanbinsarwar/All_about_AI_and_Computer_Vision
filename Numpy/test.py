import numpy as np

from PIL import Image
from matplotlib import pyplot as plt

arr = np.arange(0, 25).reshape(5, 5)
arr[:, :] = 10
print(arr)

arr = np.ones((5, 5))
arr = arr*10

np.random.seed(105)
arr = np.random.randint(low=0, high=100, size=(5, 5))
print(arr, arr.max())
print(arr.argmax())

pic = Image.open('00-puppy.jpg')
