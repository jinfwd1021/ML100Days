import numpy as np
array1 = np.array([[10, 8], [3, 5]])
result1=np.linalg.inv(array1)
print("R1:",result1)
result2=np.dot(result1,result1)
print("R2:",result2)

resultsvd=np.linalg.svd(array1)
print(resultsvd)