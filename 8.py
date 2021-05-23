import numpy as np
a = np.array([[2, 5, 3, 4, 6], [4, 3, 9, 7, 6]])
b = a[:, a.argsort()]
print(b)
