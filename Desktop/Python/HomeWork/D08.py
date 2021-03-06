import numpy as np
name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]

# 將上列 list 依照['name', 'sex', 'weight', 'rank', 'myopia']順序擺入 array，並且資料型態順序擺入[Unicode,Unicode,float,int,boolean]
list['name']=name_list
list['sex']=sex_list
list['weight']=weight_list
list['rank']=rank_list
list['myopia']=myopia_list
print(list)

np.mean(["weight"])