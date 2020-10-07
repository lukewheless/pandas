import pandas as pd
import random 

list1 = [7, 11, 13, 17]
print(pd.Series(list1, index = [1,2,3,4]))

a = pd.Series(100, range(5))
print(a)

r  = pd.Series(random.sample(range(0,100),20))
print(r.describe())

temp = pd.Series([98.6, 98.9, 100.2, 97.9], index = ['Julie', 'Charlie', 'Sam', 'Andrea'])
print(temp)

d = {'Julie':98.6, 'Charlie':98.9, 'Sam':100.2, 'Andrea':97.9}
print(pd.Series(d))