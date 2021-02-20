import numpy as np
array1 = np.array(range(30))
x=array1.reshape(5,6,order='F')
print(np.where(x%6==1))
