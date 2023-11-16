##ejemplo 1##
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()
##Example2#
##hacer cada punto una estrella##

plt.plot(ypoints, marker = '*')
