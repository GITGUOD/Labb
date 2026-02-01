import pandas as pd
data = pd.read_csv('data.csv')
a = data.info()
b = data.head()
c = data.index
d = data.columns

print(a,b,c,d)

class Lab2:
    # Exercise: filter not completed cases:

    def removeNA(data):
        data = data.dropna()
        return data
    
    def analyzePotentialOutliers(data, threshold):

        for col in data.columns:
            rawData = data[col]
            limit = threshold[threshold]

            if(rawData > limit):
                countingOutliers = countingOutliers + 1
                
        return data



