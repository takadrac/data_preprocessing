import numpy as np

a = list(np.zeros(20))
for i in range(50, 100):
    a = a[1:]
    a.append(i)
    print(a)