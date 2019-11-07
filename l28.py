import numpy as np
a=np.arange(1,25).reshape(4,6)
print(a)

print(a[1:2,1:2])
print(a[::-2,::-2])
print(a[1:5:2,1:5:2])
