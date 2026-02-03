from Lab2 import Second_Lab

import pandas as pd

data = pd.read_csv('data.csv')
a = data.info()
b = data.head()
c = data.index
d = data.columns

print(a,b,c,d)


df = pd.DataFrame({
  "a": [12, pd.NA, 10, pd.NA],
  "b": [11, pd.NA, 15, 20]
})
print(df)

print("Removed NA")
print(Second_Lab.removeNA(df))

print("Analyze Potential Outliers")
print()
thresholds = {"a": 15, "b": 25}
print(Second_Lab.analyzePotentialOutliers(Second_Lab.removeNA(df), thresholds))

print("Contributors")
print(Second_Lab.contributors('newfile.txt', 44))
#print(Second_Lab.contributors1('newfile.txt', 5))