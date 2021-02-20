import numpy as np
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])
print(np.nanmean(english_score))
print(np.nanmean(math_score))
print(np.mean(chinese_score))


english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])

print(np.nanmean(math_score))
print(np.nanmax(math_score))
print(np.nanmin(math_score))
print(np.nanstd(math_score))


Cov_EM=np.cov(english_score,math_score)
Cov_EC=np.cov(english_score,chinese_score)
check=np.greater(Cov_EM,Cov_EC)
if np.all(check)==True:
    print ('math')

else:
     print ('chinese')

