# import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()
fig, ax = plt.subplots()

language = ('Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++')
popularity = (22.2, 17.6, 8.8, 8, 7.7, 6.7)

y_pos = np.arange(len(language))


ax.barh(y_pos, popularity, align='center')

ax.set_yticks(y_pos)
ax.set_yticklabels(language)

ax.invert_yaxis()
ax.set_xlabel('Popularity')
ax.set_ylabel('Languages')
plt.grid(color='red', linestyle='--', linewidth=0.5)
fig.tight_layout()

ax.set_title(
    'popularity of Programming languages World Wide Oce 2017 compared to a year ago')

plt.show()
