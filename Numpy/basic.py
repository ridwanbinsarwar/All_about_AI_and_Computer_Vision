import numpy as np

my_list = [1, 2, 3]
my_array = np.array(my_list)
print(my_array)
arr = np.arange(0, 10, 2)
print(arr)
print(np.zeros(shape=(2, 5)))
print(np.ones(shape=(2, 5)))

np.random.seed(101)
arr = np.random.randint(0, 100, 10)
print(arr)
arr2 = np.random.randint(0, 100, 10)
print(arr2)
print(arr.max())

# max value index
print(arr.argmax())

print(arr.min())
print(arr.argmin())

print(arr.mean())
print(arr.shape)
print(arr.reshape(2, 5))

mat = np.arange(0, 100).reshape(10, 10)

print(mat)
print(mat[4, 5])
# all row column 1
print(mat[:, 1])
print(mat[0:3, 0:4])

copyOfMat = mat.copy()
mat[0:3, 0:11] = 0

print(mat)
print(copyOfMat)
