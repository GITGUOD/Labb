import subprocess
import pandas as pd
import matplotlib.pyplot as plt

# run the experiment
java = r"C:\Users\tonny\AppData\Local\Programs\Eclipse Adoptium\jdk-17.0.8.101-hotspot\bin\java.exe"
classpath = r"C:\Users\tonny\AppData\Roaming\Code\User\workspaceStorage\95abed6f19a055b53b6ee5c56cea94a4\redhat.java\jdt_ws\EDAA35-Labb_c5548da5\bin"
inFile = r"C:\Users\tonny\OneDrive\Documents\EDAA35\EDAA35-Labb\Labb_5\data1.txt"
n = 600
description = f"Collections.sort-data1.txt-{n}"
resultFile = f"{description}.csv"

print("Starting time measurements...")

subprocess.run([
    java,
    "-XX:+ShowCodeDetailsInExceptionMessages",
    "-cp", classpath,
    "Labb_5.Measure",
    inFile,
    resultFile,
    str(n)
])

# analyse the measured times
df = pd.read_csv(resultFile, index_col=0)
df.plot()
plt.savefig(f"{description}.pdf")
plt.show()
