##ejemplo 1##
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()
## ejemplo 2##

##usando lineas punteadas en ves de puntos##
plt.plot(ypoints, linestyle = 'dashed')
##Shorter Syntax##
## ejemplo##
plt.plot(ypoints, ls = ':')
