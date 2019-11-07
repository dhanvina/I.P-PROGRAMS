import numpy as np
a1=np.array([[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]])
a2=np.array([[10, 11, 12],
             [13, 14, 15],
             [16, 17, 18]])
a=np.concatenate((a1,a2),axis=1)
print(a)
