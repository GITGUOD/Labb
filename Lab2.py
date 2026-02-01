import pandas as pd
data = pd.read_csv('data.csv')
a = data.info()
b = data.head()
c = data.index
d = data.columns

print(a,b,c,d)

# Exercise: filter not completed cases:

def removeNA(data):
    data = data.dropna()
    return data