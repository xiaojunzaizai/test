import numpy as np

a = 65000
b = 10000
c = 60000
d = 50000
e = 75000
f = 45000

sal = [a,b,c,d,e,f]

g = np.average(sal)
print(g)

h = 62500
print(abs(g-h))
print(62500 - 50833)