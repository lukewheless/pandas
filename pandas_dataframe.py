import pandas as pd

grade = pd.DataFrame({"Bob": [100,100,94], 
"Chad": [87,88,97], 
"Brad": [83,100,96], "Bill": [80,100,0], "Bud": [78,99,94]})

print(grade.Bob) #grabs certain person

print(grade.iloc[1]) #pulls test 2

print(grade.iloc[[0,1], [1,4]])

