import numpy as np
a = np.array([[1, 2, 3, 4, 4], [3, 3, 4, 5, 6]])

print(a)

columnsum = a.sum(axis=0)
rownsum = a.sum(axis=1)
allSum = a.sum(axis=None)

print(columnsum)
print(rownsum)

print(allSum)
