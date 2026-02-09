import numpy as np
import scipy.stats as stats
import pandas as pd

def confidenceInterval(data, confidence=0.95):
  mean = np.mean(data)
  std_err = stats.sem(data)  # Standard error of the mean
  return stats.t.interval(confidence=confidence, df=len(data)-1, loc=mean, scale=std_err)


df = pd.read_csv("Lab_3/data.csv")

#data = np.random.normal(loc=50, scale=10, size=1000)
groupA_estimated = df[df["Group"] == "A"]["Estimate"]
groupB_estimated = df[df["Group"] == "B"]["Estimate"]
groupA_actual = df[df["Group"] == "A"]["Actual"]
groupB_actual = df[df["Group"] == "B"]["Actual"]

print("Grupp A (uppskattad tid):", confidenceInterval(groupA_estimated))
print("Grupp A (verklig tid):", confidenceInterval(groupA_actual))


print("Grupp B (uppskattad tid):", confidenceInterval(groupB_estimated))

print("Grupp B (verklig tid):", confidenceInterval(groupB_actual))


print(f"95% Confidence Interval: {confidenceInterval(df["Actual"])}")
print(f"95% Confidence Interval: {confidenceInterval(df["Estimate"])}")



#confidenceInterval(df, confidence=0.99)