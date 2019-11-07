import numpy as np
ar=np.arange(24).reshape(4,6)
print(np.hsplit(ar,2))
print(np.hsplit(ar,3))
print(np.hsplit(ar,2))
print(np.hsplit(ar,4))
