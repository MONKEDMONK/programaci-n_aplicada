##ejemplo1##
from numpy import random

x = random.pareto(a=2, size=(2, 3))

print(x)

##Visualization of Pareto Distribution##
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.pareto(a=2, size=1000), kde=False)

plt.show()
