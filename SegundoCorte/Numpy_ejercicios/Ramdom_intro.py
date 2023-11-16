                                      ###Generate Random Number####
from numpy import random

x = random.randint(100)

print(x)
                                        ###Generate Radom float###
from numpy import random

x = random.rand()

print(x)
                                      ##Generate Random Array##
from numpy import random

x=random.randint(100, size=(5))

print(x)
##ejemplo##
from numpy impor random
x=random.randint(100,size(3,5))
print(x)
                                              ##Floats##
from numpy import random

x = random.rand(5)

print(x)
##ejemplo 2###
from numpy import random

x = random.rand(3, 5)

print(x)
                              ##Generate Random Number From Array##
from numpy import random

x = random.choice([3, 5, 7, 9])

print(x)
###exapmle 2###
from numpy import random

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)

