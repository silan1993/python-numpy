# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
x1 = [10, 20, 30]
y1 = [20, 40, 10]

x2 = [10, 20, 30]
y2 = [40, 10, 30]

plt.xticks([10, 15, 20, 25, 30])
plt.yticks([10, 15, 20, 25, 30, 35, 40])

plt.plot(x1, y1, 'b-.', x2, y2, 'r--')
plt.show()
