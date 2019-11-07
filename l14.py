import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
a2=np.array([[11,22,33],[44,55,66],[77,88,99]])
a=np.concatenate((a1,a2),axis=0)
print(a)
