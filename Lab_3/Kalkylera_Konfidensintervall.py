import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

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

print("Grupp A (uppskattad tid) where first nbr is the lower end and second is upper::", confidenceInterval(groupA_estimated))
print("Grupp A (verklig tid) where first nbr is the lower end and second is upper::", confidenceInterval(groupA_actual))


print("Grupp B (uppskattad tid) where first nbr is the lower end and second is upper::", confidenceInterval(groupB_estimated))

print("Grupp B (verklig tid) where first nbr is the lower end and second is upper::", confidenceInterval(groupB_actual))


print(f"95% Confidence Interval where first nbr is the lower end and second is upper: {confidenceInterval(df['Actual'])}")
print(f"95% Confidence Interval where first nbr os the lower end and second is upper: {confidenceInterval(df['Estimate'])}")

mean_estA = groupA_estimated.mean()
mean_actA = groupA_actual.mean()
mean_estB = groupB_estimated.mean()
mean_actB = groupB_actual.mean()
mean_diffA = mean_estA - mean_actA
mean_diffB = mean_estB - mean_actB
print(f"Mean difference for Group A (Estimated - Actual): {mean_diffA}")
print(f"Mean difference for Group B (Estimated - Actual): {mean_diffB}")

# A
plt.bar(["Estimated", "Actual"], [mean_estA, mean_actA], color=["orange", "steelblue"])
plt.ylabel("Minutes")
plt.title("Mean Estimated vs Actual Time for Group A")
plt.show()

# B
plt.bar(["Estimated", "Actual"], [mean_estB, mean_actB], color=["blue", "green"])
plt.ylabel("Minutes")
plt.title("Mean Estimated vs Actual Time for Group B")
plt.show()




#confidenceInterval(df, confidence=0.99)