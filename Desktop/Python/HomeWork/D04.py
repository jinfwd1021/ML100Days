import numpy as np
from numpy.core.defchararray import count
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])

count=0
A=np.greater(english_score,math_score)
for T in A:
    if T==True:
        count=count+1
print(count)


A=np.greater(chinese_score,math_score)
B=np.greater(chinese_score,english_score)
print(np.all([A,B]))
