import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

b = np.array([1, 2, 3])

for i in range(len(a)):
    a[i, :] = a[i, :] + b

print(a)
