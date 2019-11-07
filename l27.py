import numpy as np
a= np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array((a**2)%4)
c=np.extract(b,a)
print(c)
