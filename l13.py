import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
a=np.array((a1**2)%4)
b=np.extract(a,a1)
print(b)
