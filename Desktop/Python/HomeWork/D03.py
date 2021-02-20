import numpy as np
V1 = 20000
V0 = 20
print(20*(np.log10(V1/V0)))

# 50 = 20 * log10(V50/20)
V50=10**(50/20)*20
V30=10**(30/20)*20
print(V30/V50)