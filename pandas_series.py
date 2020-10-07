import pandas as pd

grade = pd.Series([87,100,94])

print(grade)

array = pd.Series(98.6, range(3))

print(array)

print(grade.describe())

grades = pd.Series([87,100,94], index = ["Hannah", "Avery", "Josh"])
print(grades)

hardware = pd.Series(["hammer", "saw", "wrench"])

a = hardware.str.contains("a")

print(a)






